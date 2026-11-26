---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 List-level cache representation for the preserving physical array scan. 

### `Cache`

 All five cache inputs are preserved throughout preparation. 

### `Cache.Hword`

 The words stored in the cache, before selecting their sign. 

 One real triple-production iteration: two scans, three serializers and
paid cleanup. Only a parity bit is kept outside the subroutine registers. 

 A fixed, paid iteration producing the three real scalar operands. 

### `tripleWords`

 The scalar consumer uses this same three-word order definitionally. 

 The native unary loop produces all triples in increasing binomial index. 

 Initial unary copy/parity and final stream reversal are native paid calls. 

 Complete cache-to-triple primitive program with all scans and copies paid. 

### `prepare_eval`

 The only nonempty input stacks are the retained caches, width, power,
the unary number of terms, and the unary parity exponent. 

### `prepareProgram_runsIn`

 A concrete finite program, including its final halt, with no arithmetic
oracle in the transition relation. All original cache words are retained. 
