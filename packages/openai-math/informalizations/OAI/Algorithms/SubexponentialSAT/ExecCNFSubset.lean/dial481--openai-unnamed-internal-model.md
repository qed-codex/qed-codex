---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFSubset.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFSubset.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFSubset.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual encoded clause subset testing

The fixed program uses ten Boolean registers and eight Boolean stacks. The
source clause is scanned destructively on stack 0. Stack 2 preserves the entire
encoded target clause. All comparisons use the proved encoded membership
program, after a real preserving copy of the target.


### `memberCall_eval`

 The real membership program lifted into the subset caller. Only its assigned
ports change; its output bit and residual sizes are explicit. 

### `mark`

 Remember that the current source literal is absent from the target. 

### `callback`

 Each source literal invokes a real copy, encoded membership scan, and three
cleanup loops. The instruction sequence is independent of both clauses. 

### `ports`

 The outer iterator scans the source clause, stopping at its first literal
that the concrete membership program cannot find in the preserved target. 

### `finish`

 Invert the missing-literal flag and expose the answer as an output bit. 

### `budget_le`

 The bound accounts for every parsed bit, target copy, membership scan,
cleanup instruction, and loop test in the fixed subset program. 

### `subsetProgram`

 A single finite instruction table implements all runtime subset instances. 

### `rawInput`

 The raw input places the entire target record list in a frame, followed by
the source record list. This has a fixed schema independent of either clause. 

### `rawSubset_runsIn`

 The single raw input is parsed by the actual fixed program; no external
preparation of the clause stacks is assumed. The output is marshalled on stack1. 

### `natSubset_primitive_outputs`

 Natural-number literal codes are represented by their actual unary bit
strings, and the machine's answer agrees with the source-level list predicate. 

### `literalSubset_primitive_outputs`

 The literal-code map is injective, so the same fixed machine implements
clause inclusion for bounded-variable SAT literals. 
