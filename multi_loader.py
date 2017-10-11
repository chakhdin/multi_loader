import argparse
import json
import urllib.request
import time

from binascii import a2b_hex, b2a_hex
from blockchain_parser.block import Block
from bitcoinrpc.authproxy import AuthServiceProxy
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# filename = 'c:/files/medium.00000000000000000159565038ba1aec4bb9cc245f43fa3c2eed7ab0154ca40e.txt'
# txtFile = open(filename, 'r')
#
#
# i = 0
# # Iterate through each make in text file
# for line in txtFile:
#     rawText = line.strip()
#     i = i + 1
# txtFile.close()


class SQLLoader(object):
    def __init__(self, rawHex):
        self.raw_ex = rawHex

    @classmethod
    def from_hex(cls, hex_):
        return cls(hex_)

    @classmethod
    def load(cls, block_index, seq, id):
        #print(len(rawHex))
        block = Block.from_hex(rawHex)

        print(block.header.timestamp)
        print(block.hash)
        print(block.height)


        with open(dir_path+'/files/header'+str(id)+'.txt','a') as header_file:
            with open(dir_path+'/files/tx'+str(id)+'.txt','a') as tx_file:
                with open(dir_path+'/files/input'+str(id)+'.txt','a') as inp_file:
                    with open(dir_path+'/files/output'+str(id)+'.txt','a') as outp_file:
                        with open(dir_path+'/files/addr'+str(id)+'.txt','a') as addr_file:

                            print("{},{},{},{},{},{},{},{},{},{},{},{}".format(seq.header_seq,
                                                                            block.header.version,
                                                                            block.header.previous_block_hash,
                                                                            block.header.merkle_root,
                                                                            block.header.timestamp,
                                                                            block.header.bits,
                                                                            block.header.nonce,
                                                                            block.n_transactions,
                                                                            block.hash,
                                                                            block.height if block.height is not None else '',
                                                                            block_index,
                                                                            block.size),file=header_file)

                            for tx in block.transactions:
                                print("{},{},{},{},{},{},{},{}".format(seq.header_seq,
                                                                        seq.tx_seq,
                                                                        tx.hash,
                                                                        tx.version,
                                                                        tx.n_inputs,
                                                                        tx.n_outputs,
                                                                        tx.locktime,
                                                                        "Y" if tx.is_coinbase() else "N"), file = tx_file)

                                i = 0
                                for inp in tx.inputs:
                                    print("{},{},{},{},{},{},{},{},{}".format(seq.header_seq,
                                                                               seq.tx_seq,
                                                                               seq.inp_seq,
                                                                               i,
                                                                               inp.transaction_hash,
                                                                               inp.transaction_index,
                                                                               inp._script_length,
                                                                               inp.sequence_number,
                                                                               b2a_hex(inp.script.hex).decode('utf8')),file=inp_file)

                                    i += 1
                                    seq.inp_seq += 1



                                i = 0
                                for outp in tx.outputs:
                                    print("{},{},{},{},{},{},{},{},{}".format(seq.header_seq,
                                                                              seq.tx_seq,
                                                                              seq.outp_seq,
                                                                              tx.hash,
                                                                              i,
                                                                              outp.value,
                                                                              outp._script_length,
                                                                              outp.type,
                                                                              b2a_hex(outp.script.hex).decode('utf8')), file=outp_file)


                                    j = 0
                                    for addr in outp.addresses:
                                        print("{},{},{},{},{},{},{},{},{},{}".format(seq.header_seq,
                                                                          seq.tx_seq,
                                                                          seq.outp_seq,
                                                                          seq.addr_seq,
                                                                          tx.hash,
                                                                          i,
                                                                          j,
                                                                          b2a_hex(addr.public_key).decode('utf8') if addr.public_key is not None else '',
                                                                          addr.address,
                                                                          addr.type), file=addr_file)
                                        j += 1
                                        seq.addr_seq += 1
                                    i += 1
                                    seq.outp_seq += 1
                                seq.tx_seq += 1
                            seq.header_seq += 1

def getBlockHash(height):
    url = 'https://blockchain.info/block-height/' + str(height) + '?format=json'
    blk = urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(blk)

    res = data["blocks"][0]["hash"]
    return res

def getBlockHashRPC(ac, height):

    r = ac.getblockhash(height)

    return r

def getRawBlock(hsh):
    rt = urllib.request.urlopen("https://blockchain.info/rawblock/" + hsh + "?format=hex").read()
    return rt

def getRawBlockRPC(ac, hsh):
    rt = ac.getblock(hsh, False)
    return rt

class Sequences:
    def __init__(self, id):
        self.header_seq = 100000000000 * (id - 1)
        self.tx_seq = 100000000000 * (id - 1)
        self.inp_seq = 100000000000 * (id - 1)
        self.outp_seq = 100000000000 * (id - 1)
        self.addr_seq = 100000000000 * (id - 1)

#access = AuthServiceProxy("http://xenoky:8Bs6KskKBW28sb9fqePjkfhF23i7F6rk5@10.5.68.175:8332")
access = AuthServiceProxy("http://bitcoinrpc:a759assorhereasfae5@163.172.139.9:18332")
#print(dir_path)

parser = argparse.ArgumentParser(description='Process some blocks.')
parser.add_argument('start', type=int, help='start block inde')
parser.add_argument('end', type=int, help='end block inde')
parser.add_argument('id', type=int, help='process sequence')
args = parser.parse_args()

#print (args.start)
#print (args.end)

seq = Sequences(args.id)

for jj in range(args.start, args.end):
    print(jj)
    ok = False
    while not ok:
        try:
#            hs = getBlockHash(jj)
            hs = getBlockHashRPC(access, jj)
#            rawText = getRawBlock(hs)
            rawText = getRawBlockRPC(access, hs)
            ok = True
        except Exception as e:
            print(e.args)
            ok = False
            time.sleep(10)
            #access = AuthServiceProxy("http://xenoky:8Bs6KskKBW28sb9fqePjkfhF23i7F6rk5@10.5.68.175:8332")
            access = AuthServiceProxy("http://bitcoinrpc:a759assorhereasfae5@163.172.139.9:18332")

    rawHex = a2b_hex(rawText)
    db = SQLLoader.from_hex(rawHex)
    try:
        db.load(jj, seq, args.id)
    except Exception as e:
       print(rawText)
       raise e
       quit(0)


