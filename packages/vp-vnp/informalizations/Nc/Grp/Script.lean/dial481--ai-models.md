---
{
  "module": "Nc/Grp/Script.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Script.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Script.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Scripts

The script of a group is a list of instructions for the program GROUP. Keys are bit lists (paths in a trie); contents of
units are lists of `ub` bits. All bit lists are `ofBits`, all small numbers `num`, all lists `listT`.


### `Body`

 What a base party writes and reads. `flags`: for every tape (in the order of `univ.toList`) and every partner, **in
reverse order**: 0 = writes nothing, 1 = writes something, 2 = anything. `kR`, `kC`: for every partner (in order) the keys
of the units of the string to the partner, and from the partner. 

### `Body.flags`

 row data 

### `Body.kR`

 keys of units written 

### `Body.kC`

 keys of units read 

### `Ins`

 Instructions. 

### `Ins.block`

 a block, from state number `q` to state number `q'` 

### `Ins.input`

 an input party: its letters (their codes), **in reverse order** 

### `Ins.both`

 the contents at two keys agree 

### `Ins.one`

 the content at a key is `w` 

### `Ins.role`

 a role, number `j` in the list of the roles of all laws, with `t` units. `slots`: for every slot (in the order of
  `univ.toList`) the keys of the units given, **in reverse order** (what is missing to `t` units is read as zeros). `keys`:
  for every channel (in the order of `univ.toList`) the keys of the new units. 

### `keysT`

 Lists of keys. 

### `tree`

 As a tree. 

### `tree`

 As a tree. 

### `scriptT`

 The argument of GROUP: `T` and `ub` in binary (most significant bit first), and the instructions. 

### `bval`

 The value of a binary number, most significant bit first. 

### `rowFlag`

 The flag of a partner. 

### `bodyOf`

 The body of the instruction of a base party. `dkey`: keys of the second copies of the units from a party to
itself. 

### `baseIns`

 The instructions of a base party. 

### `roleIns`

 The instruction of a role. 

### `endIns`

 The instructions for the current units in the end. 

### `script`

 **The script of a group.** 
