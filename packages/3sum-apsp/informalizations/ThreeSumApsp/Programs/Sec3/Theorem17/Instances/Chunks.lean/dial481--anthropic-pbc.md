---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Chunks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Chunks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Chunks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of the chunks

Proof of Theorem 17: "cut it into chunks of at most n²/√D query pairs".  chunks(cls, p, cap, cr, cl,
cw) goes through the `p` classes, whose starts are in the `p + 1` cells from `cls`, cuts each of
them into chunks of at most `cap` places, and writes the residues, the starts and the lengths of the
chunks to `cr`, `cl` and `cw`; the residue of a chunk is the number `rho < p` of its class.  It
returns the number of chunks (`chunks_meets`).  The proof follows the program: one chunk
(`chunksRound_runs`), the chunks of one class (`chunksClass_ends`), all classes.


### `Cls`

 The locals of `chunks`.  The arguments: the address of the starts of the classes, the number `p`
of classes, the largest size `cap` of a chunk, and the addresses of the three tables.  Then the
residue, the start of the next chunk, the end of the class, the number of chunks so far, and the
length of the chunk. 

### `chunksRound`

 One chunk: len := min(cap, end - pos); the three tables get (rho, pos, len) at place cnt;
cnt := cnt + 1; pos := pos + len. 

### `chunksClass`

 The chunks of the class rho: pos := cls[rho]; end := cls[rho + 1]; while pos < end: one
chunk. 

### `chunksBody`

 chunks(cls, p, cap, cr, cl, cw). 

### `tChunks`

 The time of chunks, for p classes and nCh chunks. 

### `ChunksArgs`

 The arguments of chunks; the room `R` of each of the three tables; the list `C` of the starts of
the classes, which stands at `cls`, and a bound `B` on them. 

### `ChunksArgs.vals`

 The values of the arguments of chunks. 

### `ChunksArgs.locals`

 The locals of chunks: the arguments and the five locals that change. 

### `ChunksArgs.table`

 The table that chunks writes. 

### `ChunksArgs.Same`

 Only cells of the three tables have changed. 

### `ChunksPre`

 What chunks assumes: the starts, at most B, at cls; room for R chunks in each of the three
tables; the areas lie apart and inside the memory. 

 ## The pure side 

### `length_chunksOf`

 A class of `hi - lo` places has `⌈(hi - lo)/cap⌉` chunks. 

### `chunkRow`

 The chunks of the class number rho. 

### `tabAt`

 The table when the classes before rho and i chunks of the class rho have been handled. 

### `tabAt_zero_zero`

 At the start the table is empty. 

### `tabAt_end`

 After all classes the table is complete. 

### `tabAt_row`

 After the last chunk of a class the next class begins. 

### `tabAt_succ`

 One more chunk of the class `rho`. 

### `length_tabAt_lt`

 As long as a chunk is missing, the table is shorter than the complete one. 

### `sum_chunks_rounds`

 The time of the rounds, added up: 37 steps for each chunk and 24 for each class. 

 ## The tables in the memory 

### `TabInv`

 The three tables hold the list T, and nothing else has changed. 

### `TabInv.push`

 One more chunk: each table gets one more entry, and the writes to the other two tables do not
touch it. 

### `ChunksPre.start`

 A start of a class, read from a memory in which only the tables have changed. 

 ## The program 

### `chunksRound_runs`

 One chunk. 

### `ChunksInv`

 The state of `chunks` when the residue is `rho` and the three tables hold the list `T`. 

### `chunksClass_ends`

 The chunks of one class. 

### `chunks_meets`

 **chunks** writes the table of the chunks and returns their number. 
