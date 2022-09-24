# EVM Bytecode Optimisation

This repository contains the EVM bytecode optimisation for a Fibonacci function.
Using opcodes from the Ethereum yellow paper, the challenge of this was to create a function to output the Fibonacci number at a given index using the shortest bytecode possible.

## Constraints
* Input is a `uint256` representing an index
* Return a `uint256` representing the Fibonacci number

## Contract source
High level code of the Fibonacci function:
`src/Contract.sol`

## Optimised bytecode
Optimised bytecode representation:
`src/bytecode_opt`