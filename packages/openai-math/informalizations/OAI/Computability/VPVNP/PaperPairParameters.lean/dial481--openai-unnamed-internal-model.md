---
{
  "module": "OAI/Computability/VPVNP/PaperPairParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PaperPairParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PaperPairParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer parameters of the fixed live and virtual machines

The rational exponents chosen by the compressor have fixed positive
numerators and denominators. Using them in the integer floor and ceiling
algorithms gives exactly the analytic block and bucket counts of §9.1 at
every length. After choosing the address exponent, one threshold supplies
the live and virtual word capacities, the exponent no-overflow margin,
and enough fresh lane coordinates.


### `Ratio`

 A positive rational strictly below one in the fixed program's operand format. 

### `Ratio.num`

 Positive integer numerator in the program's representation of a ratio between zero and
  one. 

### `Ratio.den`

 Positive integer denominator, strictly larger than the numerator, used by the program's
  rounded integer arithmetic. 

### `Ratio.ofRat`

 Encodes a positive rational below one by its natural numerator and denominator, preserving
its value as a real number. 

### `blockRatio`

 Operand pair representing the block exponent θ in the fixed program. 

### `liveRatio`

 Operand pair representing the live-bucket exponent 1 − δ in the fixed program. 

### `liveCapacity`

 The power of two obtained by rounding (1 − δ) log₂ n upward to an integer using the
live-ratio operands. 

### `eventually_liveCapacity_ge`

 Any fixed number of probes fits the live bucket at sufficiently large lengths. 

### `eventually_numeric`

 Address/counter and geometry premises in the physical local certificate,
before any particular algebra, path or prime is chosen. 

### `laneLabels`

 Number the reserved lane coordinates after the base coordinates, using
exactly the number consumed by the selected blocks. 
