---
{
  "module": "proof/consequences/FreeCode/Reader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Reader.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Reader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 with the code that does not depend on k: a reader

No sentence of the paper stands behind this file: the paper fixes no code. `readFree` reads 1ⁿ0 and
then goes once through the remaining bits, one step (`stepR`) per bit, keeping this state:
two bits that say where it is (between clauses; in a clause, before a mark; inside the bits of a
literal; past the end of the formula), the bits of the literal that is being read, the literals of
the clause that is being read, and the clauses read so far; all three lists last member first, and a
literal as its word of bits.
At the end the lists are turned round and every word of bits is read as a literal.
`readFree_enc_append`: on the code of φ followed by ANY bits the reader returns (n in unary, φ with
numbers as variables). `reads_readFree` is the case of no further bits. That the reader is
polynomial time is proved in proof/consequences/FreeCode/ReaderCert.lean. 

### `RState`

 The state of the reader: two bits for the place (00 between clauses, 01 in a clause before a
mark, 10 inside a literal, 11 past the end), the bits of the literal being read, the literals of the
clause being read, the clauses read; each list last member first. 

### `stepR`

 One bit e is read; w is the number of bits of a literal. 

### `scanR`

 The state after all bits that follow 1ⁿ0 have been read. 

### `readFree`

 The reader: n in unary, and the clauses read, every word of bits as a literal. 

### `takeWhile_header`

 The ones in front of the first zero. 

### `dropWhile_header`

 What stands from the first zero on. 

### `foldl_bits`

 Inside a literal: when the bits still to come fill the literal up to w bits, the reader ends in
the clause, with the word of the literal (last bit first) put on the clause. 

### `foldl_lit`

 In a clause: the mark 1 and the w bits of a literal put the word of the literal (last bit first)
on the clause. 

### `foldl_lits`

 In a clause: the literals of C, each behind its mark, are put on the clause. 

### `foldl_clause`

 Between clauses: the code of a clause puts the clause on the list of clauses. 

### `foldl_clauses`

 Between clauses: the codes of the clauses of φ put them on the list of clauses. 

### `foldl_done`

 Past the end of the formula nothing changes. 

### `scanR_enc_append`

 The state of the reader after the code of φ followed by any bits u. 

### `readFree_enc_append`

 **The reader on a code followed by any bits**: it returns n in unary and φ with numbers as
variables. 

### `reads_readFree`

 `readFree` reads the code. 
