---
{
  "module": "OAI/Computability/VPVNP/LiveFirstTailHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The first evaluator group after the initial-state write

At the midpoint the incoming cut still uses the pair format. The first
tail group therefore receives the accumulated exponents and the copied
advice in their physical header arrays. The router and the state writer
touch only the stage tag and old control word, leaving every old tape cell
blank and both input arrays intact for the advice and input sweeps.


### `size`

 The header dimensions evaluated at the physical group's constants and geometry. 

### `labelCount`

 The group's evaluated number of exponent labels. 

### `exponentWidth`

 The group's evaluated digit width for each exponent. 

### `middle`

 The physical group index of the first evaluator group, at the start of the second half. 

### `middleWords`

 The typed exponent field of the same midpoint cut used in
`groupEvaluation` and in the evaluator's initial code. 

### `middle_bits`

 The physical input bank is precisely the last vector of first-half
counters, including the low-endian order of the bits within each label. 

### `prepared`

 After the nonempty evaluator's first state write, all arrays consumed
by the packing and input stages are in their concrete program locations. 
