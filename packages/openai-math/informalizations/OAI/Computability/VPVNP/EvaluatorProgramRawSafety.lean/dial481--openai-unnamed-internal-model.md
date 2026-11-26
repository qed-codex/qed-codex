---
{
  "module": "OAI/Computability/VPVNP/EvaluatorProgramRawSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramRawSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramRawSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All-branch resources from the raw input to the monomial result

The parser and native converter have polynomial deterministic clocks. The
digit traversal may run for exponentially many steps while respecting its
polynomial stack bound. Each framed callback retains its safety certificate
on both successors of every binary choice.


### `Bounded.onPorts_frame`

 Preserve the stopping and peak-space contract under an embedding of
stack banks which commutes with every physical read and write. 

### `nativeSpace`

 Input sizes and converter clock are polynomial in the exponent width,
label count, divisor bit width and callback storage. 

### `inputLengthBound`

 Upper bound on the encoded input length from the advice size, number of labels and binary
exponent width. 

### `readerBudget`

 Time allowance for parsing the tagged raw input, bounded by twice its length bound plus one
instruction. 

### `rawSpace`

 Stack-space bound covering the raw input, parser workspace and the subsequent converted
monomial execution. 

### `rawSpace_le_power`

 The closed physical storage bound is a degree-four polynomial in the
label count, exponent width, divisor width, callback space, and advice size. 

### `native_bounded`

 All paths of the native converter and the physical scheduler satisfy
the resource bound, including paths that reject inside a callback. 

### `raw_bounded_of_native`

 Load the raw stream with its deterministic polynomial-space parser, then
preserve the resource certificate of the entire native machine. 

### `raw_space_clock`

 A physical stopping clock and a polynomial bound on every reachable
stack in the machine starting on the sole raw input tape. 
