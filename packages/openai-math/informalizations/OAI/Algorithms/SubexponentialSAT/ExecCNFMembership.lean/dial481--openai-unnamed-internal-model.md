---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFMembership.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFMembership.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFMembership.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Encoded CNF membership building blocks

Fixed ports: source 0, reversed current payload 1, preserved reversed query 2,
query copy 3, and temporary stack 4. Register 4 is the answer; registers 5 and
6 are the outer-list tag and presence flag. Registers 0--3 are work bits.


### `copyQueryProgram`

 The query remains on port 2; a forward-order copy is made on port 3. 

### `clearProgram`

 Clearing is an actual two-instruction loop followed by a halt/return. 

### `callback`

 Compare the parsed reversed payload against a fresh copy of the query,
then clear both inspected work strings, including early-mismatch residuals. 

### `callback_eval`

 Actual call traces, not a semantic equality instruction, implement the
callback. The preserved query and source suffix make another iteration safe. 

### `ports`

 The runtime query is on stack 2; these ports are fixed for every query. 

### `budget_le`

 Coarse polynomial bound for the iterator's complete per-record budget. 

### `membership`

 The emitted bit is in stack 1. The encoded source is scanned destructively,
while stack 2 retains the reversed runtime query. 

### `membershipProgram`

 This instruction table has fixed size, independent of both runtime inputs. 

### `rawInput`

 Single-tape input: one framed query, followed by the framed record list. 

### `cleanup`

 Discard the unscanned suffix and retained query after emitting the answer. 

### `literal_primitive_contains`

 The concrete bit program implements the earlier executable literal scan.
Arbitrary natural literal codes are compared through their actual encodings. 
