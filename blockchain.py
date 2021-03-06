from flask import Flask, render_template, redirect, url_for
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
import winsound

node = Flask(__name__)

#IPaddress = '192.168.1.111'
IPaddress = '10.138.111.250'
#IPaddress = '192.168.1.253'
#IPaddress = '192.168.1.100'

# Define what a block is
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
username = ''
username1 = ''
username2 = ''
username3 = ''
username4 = ''
username5 = ''
accountID = ''
accountID1 = ''
accountID2 = ''
accountID3 = ''
accountID4 = ''
accountID5 = ''
currentCoins1 = 500
currentCoins2 = 500
currentCoins3 = 500
currentCoins4 = 500
currentCoins5 = 500

@node.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        global username
        global username1
        global username2
        global username3
        global username4
        global username5
        global accountID
        global accountID1
        global accountID2
        global accountID3
        global accountID4
        global accountID5
        accountID = str(request.form['myList'])
        username = str(request.form['name'])
        if accountID == 'Nokia':
            username1 = username
            accountID1 = accountID
        if accountID == 'User2':
            username2 = username
            accountID2 = accountID
        if accountID == 'User3':
            username3 = username
            accountID3 = accountID
        if accountID == 'User4':
            username4 = username
            accountID4 = accountID
        if accountID == 'User5':
            username5 = username
            accountID5 = accountID
        return redirect('http://' + IPaddress + ':5000/txion' +accountID)

    return render_template('signup.html')


@node.route('/txionNokia', methods=['GET','POST'])
def transaction():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))
        mine()
        winsound.PlaySound('money', winsound.SND_FILENAME)
        global currentCoins1
        global currentCoins2
        global currentCoins3
        global currentCoins4
        global currentCoins5
        addedCoins2 = 0
        addedCoins3 = 0
        addedCoins4 = 0
        addedCoins5 = 0
        coinAmount = int(request.form['amount'])
        currentCoins1 = currentCoins1 - coinAmount
        userTo = str(request.form['myList1'])
        if userTo == 'User2':
            addedCoins2 = coinAmount
            currentCoins2 = currentCoins2+addedCoins2
        if userTo == 'User3':
            addedCoins3 = coinAmount
            currentCoins3 = currentCoins3+addedCoins3
        if userTo == 'User4':
            addedCoins4 = coinAmount
            currentCoins4 = currentCoins4+addedCoins4
        if userTo == 'User5':
            addedCoins5 = coinAmount
            currentCoins5 = currentCoins5+addedCoins5
        #return redirect('http://' + IPaddress + ':5000/txionNokia')
        return render_template('successful.html')

    return render_template('txion1.html', username1=username1, currentCoins1=currentCoins1, accountID1=accountID1)


@node.route('/txionUser2', methods=['GET','POST'])
def transaction2():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))
        mine()
        winsound.PlaySound('money', winsound.SND_FILENAME)
        global currentCoins1
        global currentCoins2
        global currentCoins3
        global currentCoins4
        global currentCoins5
        addedCoins1 = 0
        addedCoins3 = 0
        addedCoins4 = 0
        addedCoins5 = 0
        coinAmount = int(request.form['amount'])
        currentCoins2 = currentCoins2 - coinAmount
        userTo = str(request.form['myList2'])
        if userTo == 'Nokia':
            addedCoins1 = coinAmount
            currentCoins1 = currentCoins1+addedCoins1
        if userTo == 'User3':
            addedCoins3 = coinAmount
            currentCoins3 = currentCoins3+addedCoins3
        if userTo == 'User4':
            addedCoins4 = coinAmount
            currentCoins4 = currentCoins4+addedCoins4
        if userTo == 'User5':
            addedCoins5 = coinAmount
            currentCoins5 = currentCoins5+addedCoins5
        return render_template('successful.html')

    return render_template('txion2.html', username2=username2, currentCoins2=currentCoins2, accountID2=accountID2)


@node.route('/txionUser3', methods=['GET','POST'])
def transaction3():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))
        mine()
        winsound.PlaySound('money', winsound.SND_FILENAME)
        global currentCoins1
        global currentCoins2
        global currentCoins3
        global currentCoins4
        global currentCoins5
        addedCoins1 = 0
        addedCoins2 = 0
        addedCoins4 = 0
        addedCoins5 = 0
        coinAmount = int(request.form['amount'])
        currentCoins3 = currentCoins3 - coinAmount
        userTo = str(request.form['myList3'])
        if userTo == 'Nokia':
            addedCoins1 = coinAmount
            currentCoins1 = currentCoins1+addedCoins1
        if userTo == 'User2':
            addedCoins2 = coinAmount
            currentCoins2 = currentCoins2+addedCoins2
        if userTo == 'User4':
            addedCoins4 = coinAmount
            currentCoins4 = currentCoins4+addedCoins4
        if userTo == 'User5':
            addedCoins5 = coinAmount
            currentCoins5 = currentCoins5+addedCoins5
        return render_template('successful.html')

    return render_template('txion3.html', username3=username3, currentCoins3=currentCoins3, accountID3=accountID3)


@node.route('/txionUser4', methods=['GET','POST'])
def transaction4():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))
        mine()
        winsound.PlaySound('money', winsound.SND_FILENAME)
        global currentCoins1
        global currentCoins2
        global currentCoins3
        global currentCoins4
        global currentCoins5
        addedCoins1 = 0
        addedCoins2 = 0
        addedCoins3 = 0
        addedCoins5 = 0
        coinAmount = int(request.form['amount'])
        currentCoins4 = currentCoins4 - coinAmount
        userTo = str(request.form['myList4'])
        if userTo == 'Nokia':
            addedCoins1 = coinAmount
            currentCoins1 = currentCoins1+addedCoins1
        if userTo == 'User2':
            addedCoins2 = coinAmount
            currentCoins2 = currentCoins2+addedCoins2
        if userTo == 'User3':
            addedCoins3 = coinAmount
            currentCoins3 = currentCoins3+addedCoins3
        if userTo == 'User5':
            addedCoins5 = coinAmount
            currentCoins5 = currentCoins5+addedCoins5
        return render_template('successful.html')

    return render_template('txion4.html', username4=username4, currentCoins4=currentCoins4, accountID4=accountID4)


@node.route('/txionUser5', methods=['GET','POST'])
def transaction5():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        this_nodes_transactions.append(request.form.get('amount'))
        mine()
        winsound.PlaySound('money', winsound.SND_FILENAME)
        global currentCoins1
        global currentCoins2
        global currentCoins3
        global currentCoins4
        global currentCoins5
        addedCoins1 = 0
        addedCoins2 = 0
        addedCoins3 = 0
        addedCoins4 = 0
        coinAmount = int(request.form['amount'])
        currentCoins5 = currentCoins5 - coinAmount
        userTo = str(request.form['myList5'])
        if userTo == 'Nokia':
            addedCoins1 = coinAmount
            currentCoins1 = currentCoins1+addedCoins1
        if userTo == 'User2':
            addedCoins2 = coinAmount
            currentCoins2 = currentCoins2+addedCoins2
        if userTo == 'User3':
            addedCoins3 = coinAmount
            currentCoins3 = currentCoins3+addedCoins3
        if userTo == 'User4':
            addedCoins4 = coinAmount
            currentCoins4 = currentCoins4+addedCoins4
        return render_template('successful.html')

    return render_template('txion5.html', username5=username5, currentCoins5=currentCoins5, accountID5=accountID5)


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


#node.run('192.168.1.111')
node.run('10.138.111.250')
#node.run('192.168.1.253')
#node.run('192.168.1.100')
