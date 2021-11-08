from solcx import compile_standard

# error with solcx

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)


compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytcode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
print(compiled_sol)
