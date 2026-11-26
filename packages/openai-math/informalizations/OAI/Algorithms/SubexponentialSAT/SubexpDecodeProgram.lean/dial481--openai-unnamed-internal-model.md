---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDecodeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDecodeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDecodeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An actual finite program for the final count decision

The modulus and first coefficient are runtime Boolean words. The program
reduces the word modulo the modulus, then scans for a one bit. Both phases
execute inside one fixed 96-label instruction table.


### `run`

 Actual execution from a prepared coefficient and modulus. Work stacks are
empty at entry. The result is the head of stack zero; the modulus is preserved. 

### `primitive_run`

 A primitive-tape trace of this same fixed program, with its compiler cost. 

### `count_answer_iff`

 Quotient equality and the strict count bound identify the Boolean returned
by the finite program. In particular a noncanonical encoding of zero is reduced
before it is tested. 

### `prepared_run`

 The prepared coefficient representation gives a uniform quadratic bound
in its word width. This uses the actual binary modulus stored by setup. 
