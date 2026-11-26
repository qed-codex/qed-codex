---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramArithmeticNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramArithmeticNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramArithmeticNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Component: HashCircuitProgramArithmetic. All public namespaces and APIs are retained. 

 Native arithmetic wiring for the hash interpreter. Scale and normalized
addition are fixed imported instruction tables. Product is wired separately
when the native product table is supplied by its implementation module. 

### `scalePorts`

 Keep the full arithmetic cache on its low ports. 

### `addPorts`

 The normalizer's coefficient scratch17 and lookup scratch22 must not
overwrite the multiplication cache at those physical ports. 

### `weightedCore`

 Shared fixed weighted-sum core, retaining the low56 arithmetic ABI. 

### `complement`

 Input61 is replaced by one minus its value. 

### `accumulate`

 Parsed reversed weight65 becomes forward coefficient44 through an actual
transfer. The scaled clause is accumulated with the prior row dictionary. 

### `productAdapter`

 Product's local ABI isA40, B41, result42, with B preserved. The copied
operands and native result are reclaimed after moving the result to67. 

### `scale_call`

 Calling the scale table retains exactly its checked primitive trace,
with all caller stacks outside0..39 framed. 

 Component: HashCircuitProgram. All public namespaces and APIs are retained. 

 The fixed native sparse-hash row instruction table. All arithmetic
components are now concrete native programs: there are no operation-valued
parameters in `command` or `program`. The complete serialized semantic and
primitive-time theorem must additionally discharge the local callback
contracts for this table; no such theorem is asserted merely by compilation. 

### `product_call`

 The product subroutine is the real fixed sparse-product table. Its trace
is preserved by the call, and every caller stack above55 remains framed. 

 Component: HashCircuitProgramMemoryExtra. All public namespaces and APIs are retained. 

### `transfer_high_low`

 Reversal transfer consumes a high parsed payload into the low workspace. 

### `copy_high_high`

 Preserving copy between persistent interpreter words. 

### `weightedCore_lift`

 The low core's measured execution is lifted without touching high tapes. 

 Component: HashCircuitProgramWeightedCallbacks. All public namespaces and APIs are retained. 

 The two concrete weighted arithmetic adapters used by the hash evaluator.
The statements expose exact dictionary bytes and restoration of the common
arithmetic workspace. In particular they do not assume callback correctness. 

### `complement_eval`

 A cached scalar and seed are physically copied, applied and reclaimed.
For the literal-complement use they are the represented minus-one and one. 

### `accumulate_eval`

 The row adapter consumes the reversed parsed scalar and clause dictionary,
adds the scaled clause to the prior row, and leaves all other high data intact. 

 Component: HashCircuitProgramProduct. All public namespaces and APIs are retained. 

 Concrete product callback refinement. Both sparse operands are copied from
persistent interpreter stacks into the real product program. The result is
copied back, and all temporary operands are physically reclaimed. 

### `eval`

 Fully native callback theorem. The only numerical assumptions specify the
actual represented coefficient ring and runtime shapes; there is no abstract
arithmetic-command or callback-cost premise. 
