---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the four midpoint operand frames

The native initializer reads the packed prefix length at offset 22, checks
its capacity, and writes the operands of the prefix packer, input copy,
runtime skeleton and exponent scatter. Their frames start at offsets 0, 8,
13 and 17. The three holes at 5–7 and the stored length at 22 are preserved.


### `slots`

 The register-to-frame assignment for the four midpoint workers, reserving holes at offsets
5 through 7. 

### `body`

 Compute the midpoint operands and store them into their assigned slots in the shared frame. 

### `template`

 One deterministic native call. Its normal exit accepts the stage. 

### `prefixFrame`

 The five operands for packing the evaluator prefix, including source, destination, field
width, actual bit count, and row count. 

### `copyFrame`

 The five words supplying the input-copy worker with its input size, tape location, packed
advice location, field width, and prefix length. 

### `skeletonFrame`

 The runtime skeleton's two size parameters, computed base address, and total length. 

### `scatterFrame`

 The five operands used to scatter production exponents into the runtime area. 

### `published`

 The external memory after computing and writing all four midpoint operand frames. 

### `events`

 The successful initializer's complete load, calculation, and frame-store event sequence. 

### `events_cost`

 The sole length read and 19 operand writes are the only external probes. 

### `reject_frames`

 A malformed length or a zero word-width parameter rejects at any fuel and on every stream. 

### `PublishedAt`

 The exact stored frame payloads as read by the dynamic operand adapter. 
