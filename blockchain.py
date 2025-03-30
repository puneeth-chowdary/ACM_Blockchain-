import time


def calculate_block_hash(input_data):
    hash_result = 0
    for character in input_data:
        hash_result = (hash_result * 31 + ord(character)) % (10**16)  
    return str(hash_result)


class Block:
    def __init__(self, block_index, creation_time, block_data, parent_hash, proof_value):
        self.block_index = block_index  
        self.creation_time = creation_time  
        self.block_data = block_data  
        self.parent_hash = parent_hash  
        self.proof_value = proof_value  
        self.current_hash = self.generate_block_hash()  

    def generate_block_hash(self):
        block_contents = f"{self.block_index}{self.creation_time}{self.block_data}{self.parent_hash}{self.proof_value}"
        return calculate_block_hash(block_contents)


class Blockchain:
    def __init__(self):
        self.blockchain = []
        self.mining_difficulty = 2  
        self.initialize_genesis_block()  

    def initialize_genesis_block(self):
        genesis_data = "Genesis Block"
        initial_block = Block(0, time.time(), genesis_data, "0", 0)
        self.blockchain.append(initial_block)

    def get_previous_block(self):
        return self.blockchain[-1]  

    def mine_new_proof(self, previous_proof):

        current_proof = 0
        max_attempts = 100000 
        while not self.validate_proof(current_proof, previous_proof):
            current_proof += 1
            if current_proof > max_attempts:
                print("Mining took too long. Consider adjusting difficulty!")
                return None  # Abort mining
        return current_proof

    def validate_proof(self, current_proof, previous_proof):
        proof_attempt = f"{current_proof}{previous_proof}"
        attempt_hash = calculate_block_hash(proof_attempt)
        return attempt_hash[:self.mining_difficulty] == "0" * self.mining_difficulty

    def add_new_block(self, transaction_data):
        last_block = self.get_previous_block()
        new_proof = self.mine_new_proof(last_block.proof_value)
        if new_proof is not None:  
            new_block = Block(len(self.blockchain), time.time(), transaction_data, last_block.current_hash, new_proof)
            self.blockchain.append(new_block)

    def display_blockchain(self):
        for block in self.blockchain:
            print(f"Block Index: {block.block_index}")
            print(f"Creation Time: {block.creation_time}")
            print(f"Block Data: {block.block_data}")
            print(f"Parent Hash: {block.parent_hash}")
            print(f"Proof Value: {block.proof_value}")
            print(f"Current Hash: {block.current_hash}")




if __name__ == "__main__":
    my_blockchain = Blockchain()

