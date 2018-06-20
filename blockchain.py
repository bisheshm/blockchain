from flask import Flask, render_template
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date

node = Flask(__name__)


# Define what a Snakecoin block is
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha.hexdigest()


# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), 0, "0")


# A completely random address of the owner of this node
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
# This node's blockchain copy
blockchain = []
blockchain.append(create_genesis_block())
# Store the transactions that
# this node has in a list
this_nodes_transactions = []
# Store the url data of every
# other node in the network
# so that we can communicate
# with them
peer_nodes = []
# A variable to deciding if we're mining or not
mining = True


@node.route('/txion', methods=['GET','POST'])
def transaction():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))


    return '''  <head>
                <h2 align="center"; style="color:#124191">Make a Transaction</h1>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
                </head>
                <br>
                <form method="POST" align="center">
                      From: <input type="text" name="from"><br>
                      <br>
                      To: <input type="text" name="to"><br>
                      <br>
                      Amount: <input type="text" name="amount"><br>
                      <br>
                      <input class="btn btn-primary" type = "submit" value="Submit"><br>
                </form>'''


@node.route('/')
def get_blocks():
  chain_to_send = blockchain
  blocklist = ""
  for i in range(len(chain_to_send)):
    block = chain_to_send[i]
    block_index = str(block.index)
    block_timestamp = str(block.timestamp)
    block_data = str(block.data)
    block_hash = block.hash
    assembled = [block_index, block_timestamp, block_hash, block_data]
    if blocklist == "":
      blocklist = assembled
    else:
      blocklist += assembled
  numRows = int(len(blocklist) / 4)

  index = blocklist[::4]
  timestamp = blocklist[1::4]
  hashlist = blocklist[2::4]
  coinAmount = blocklist[3::4]

  return render_template('index.html', numRows=numRows, index=index, timestamp=timestamp, hashlist=hashlist, coinAmount=coinAmount)


def find_new_chains():
    # Get the blockchains of every
    # other node
    other_chains = []
    for node_url in peer_nodes:
        # Get their chains using a GET request
        block = requests.get(node_url + "/blocks").content
        # Convert the JSON object to a Python dictionary
        block = json.loads(block)
        # Add it to our list
        other_chains.append(block)
    return other_chains

def consensus():
  # Get the blocks from other nodes
  global blockchain
  other_chains = find_new_chains()
  # If our chain isn't longest,
  # then we store the longest chain
  longest_chain = blockchain
  for chain in other_chains:
    if len(longest_chain) < len(chain):
      longest_chain = chain
  # If the longest chain isn't ours,
  # then we stop mining and set
  # our chain to the longest one
  blockchain = longest_chain

def proof_of_work(last_proof):
  # Create a variable that we will use to find
  # our next proof of work
  incrementor = last_proof + 1
  # Keep incrementing the incrementor until
  # it's equal to a number divisible by 9
  # and the proof of work of the previous
  # block in the chain
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    incrementor += 1
  # Once that number is found,
  # we can return it as a proof
  # of our work
  return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  # Find the proof of work for
  # the current block being mined
  # Note: The program will hang here until a new
  #       proof of work is found

  # Once we find a valid proof of work,
  # we know we can mine a block so
  # we reward the miner by adding a transaction
  # Now we can gather the data needed
  # to create the new block
  if not this_nodes_transactions:
      new_block_data = 0
  else:
      new_block_data = this_nodes_transactions[-1]

  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  # Empty transaction list
  # Now create the
  # new block!
  this_nodes_transactions[:] = []
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  # Let the client know we mined a block
  return json.dumps({
      "index": new_block_index,
      "timestamp": str(new_block_timestamp),
      "data": new_block_data,
      "hash": last_block_hash
  }) + "\n"


node.run('192.168.1.111')

