---
{
  "module": "proof/machines/Wrap/CodingExists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/CodingExists.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/CodingExists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Every machine with finite alphabets has a coding of its configurations

Labels, states and symbols are numbered. A configuration is written as the pair of the numbers of
its label and state, and the list of its stacks, in a fixed order, each stack as the list of the
numbers of its symbols (`repOf`).
One step sees only the label, the state and the top d symbols of every stack
(`CircuitLowerBound.Tab.stay_eq`). These make a configuration of their own, `top M c`, and there are
finitely many of them. So the step on values (`stepOf`) cuts the top d
numbers off every stack, looks the result up in a fixed finite table, which holds the value of the
next configuration, and puts the stacks found there in front of what was left of the old stacks.
`coding_exists` collects the fields of `Coding M`; everything before it stands in the namespace
`Wrap.Conf`. 

 ### Numbers for the elements of a finite type 

### `num`

 The number of an element of a finite type, in some fixed order of the type. 

### `num_injective`

 Different elements have different numbers. 

### `num_lt`

 The numbers are below the number of elements. 

 ### Sizes of lists 

### `size_nat_le`

 If n ≤ b, the size of n is at most the number of bits of b, plus 1. 

### `size_append`

 The sizes of two lists add up to the size of the joined list and 1. 

### `size_drop_le`

 Dropping entries does not make a list larger. 

### `size_le_of_forall`

 A list whose entries have size at most B has size at most (number of entries)·(B + 1) + 1. 

### `size_map_le`

 If every entry grows by at most e, the list grows by at most (number of entries)·e. 

### `polyT_map_const`

 A fixed list of polynomial-time functions, applied to one argument, is polynomial-time. 

 ### Configurations as values 

### `ks`

 The names of the stacks, each once, in a fixed order. 

### `mem_ks`

 Every stack is in the list. 

### `top`

 The configuration made of the label, the state and the top d symbols of every stack, where d is
the number of symbols that one step can see. 

### `nxt_caseOf`

 The step on the tops alone, as the table of the machine has it, is the step of the configuration
made of the tops. 

### `stay_eq_top`

 One step: do the step on the tops alone, and put the new tops in front of what lies below the
top d symbols. 

### `length_stay_top_le`

 After a step on the tops alone a stack has at most 2d symbols. 

### `sym`

 The number of a symbol of stack k. 

### `sym_injective`

 Different symbols of a stack have different numbers. 

### `sym_lt`

 The numbers of the symbols are below the number of all symbols of all stacks. 

### `bnd`

 A bound on the size of every number that stands for a label, a state or a symbol. 

### `size_lab_le`

 The number of a label, or of «halted», has size at most the bound. 

### `size_var_le`

 The number of a state has size at most the bound. 

### `size_sym_le`

 The number of a symbol has size at most the bound. 

### `repOf`

 The value that stands for a configuration: the numbers of the label and of the state, and the
stacks as lists of numbers. 

### `repOf_injective`

 Different configurations have different values. 

 ### The step 

### `key`

 The first two numbers and the top d entries of every list. 

### `key_repOf`

 Cutting the value of a configuration gives the value of the configuration made of the tops. 

### `keys`

 A fixed list that holds the values of all configurations made of tops. 

### `repOf_top_mem`

 The value of a configuration made of tops is in the list. 

### `entry`

 The entry of the table at the value of a configuration: the value of the next configuration. 

### `entry_repOf`

 At the value of c the table holds the value of the configuration after c. 

### `tab`

 Reading the table, which has an entry for each value in `keys M`. 

### `tab_polyT`

 Reading the table is polynomial-time, because the table is fixed and finite. 

### `stepOf`

 One step on values: cut off the tops, look them up, put the new tops in front of the rest. 

### `stepOf_polyT`

 The step on values is polynomial-time. 

### `stepOf_repOf`

 The step on values is the step of the machine. 

 ### The start 

### `inSym`

 The number of the symbol of the input stack that stands for a bit. 

### `initOf`

 The start configuration on the bit string x, as a value: the input stack holds the numbers of
the symbols that stand for the bits of x, the other stacks are empty. 

### `initOf_polyT`

 The start on values is polynomial-time. 

### `initOf_eq`

 The start on values is the value of the start configuration of the machine. 

 ### The output 

### `outIdx`

 The place of the output stack in the list of the stacks. 

### `ks_outIdx`

 At that place stands the output stack. 

### `bitOf`

 The bit for which a symbol of the output stack stands, from the number of the symbol: a fixed
finite table. 

### `bitOf_polyT`

 Reading that table is polynomial-time. 

### `bitOf_sym`

 The table gives back the bit of a symbol. 

### `outOf`

 The output: if the first number is that of «halted», the bits of the output stack; otherwise
nothing. 

### `outOf_polyT`

 Reading the output is polynomial-time. 

### `outOf_halted`

 On a halted configuration the output is the content of the output stack, as bits. 

### `outOf_running`

 On a configuration that is not halted there is no output. 

 ### Sizes 

### `size_stack_le`

 A stack of n symbols, as a list of numbers, has size at most n·(bound + 1) + 1. 

### `size_repOf_le`

 If every stack of c has at most n symbols, the value of c has size at most 2·bnd + (number of
stacks)·(n·(bnd + 1) + 2) + 1. 

### `size_repOf_stay_le`

 A step adds at most a constant to the size of the value. 

### `size_initOf_le`

 The value of the start configuration is at most linear in the input. 

### `coding_exists`

 Every machine with finite alphabets has a coding of its configurations as values of the type
`Rep`: polynomial-time functions on values for the start, for one step and for reading the output,
and bounds on the sizes. 
