---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StructuredCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StructuredCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StructuredCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Structured invocation of existing finite bit programs

A call contains a fixed finite instruction table. Its execution premise is an
actual trace of that table, rather than a semantic or cost oracle. Compilation
relocates all its instructions and replaces each halt by a return jump. Thus
arbitrary cyclic subroutines can occur inside structured loops without manually
assigning global labels.


### `Eval`

 A call's cost is its actual instruction-trace length, including the source
halt which becomes the compiled return jump. 

### `siteEquiv`

 Finite control enumeration is computed directly from the fixed syntax. 

### `code`

 Calls use the proved concrete instruction relocation, including every
internal branch and each return instruction. 

### `eval_trace`

 Exact execution preservation, proved with the concrete subroutine linker
in the call case. 

### `compiled`

 The full finite instruction table is computably generated from the fixed
syntax and finite subroutine tables. No runtime stack data is inspected. 

### `embedState`

 Mathematical data embedding for a subroutine's assigned ports. The finite
compiled instructions use the port maps directly; they never execute this
Function.extend expression. 

### `eval_call_lifted`

 Invoke an existing smaller program using fixed injective port assignments.
Its exact trace count is retained, and all unassigned caller data is framed. 
