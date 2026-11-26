---
{
  "module": "OAI/Computability/VPVNP/LiveOutsideTailStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTailStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTailStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Resource bounds for the reports of the native tail stages

The endpoint stages issue one control-word write, and each configuration
gather contributes one report per word of the cut. The dynamic advice
prefix and the transition use the same linked reports as the path-count
handoffs. Bounds include both the outer stage dispatcher and its tag write.


### `params`

 The resource parameters for this tail execution, using the raw prefix length and the
group's label, exponent, tape, and word dimensions. 

### `packWork`

 The charge for packing the length, advice prefix, and ordinal rows and publishing their
operand frames. 

### `inputWork`

 The charge for copying the input bits, writing the runtime skeleton, and scattering the
exponents. 

### `firstBudget`

 The incoming-side budget for either a gathered configuration or an initial control write
with any required advice and input setup. 

### `lastBudget`

 The outgoing-side budget for either a gathered configuration or the final accepting control
write. 

### `callBound`

 Uniform maximum cost of one actual linked tail report. 

### `instructionBound`

 The advice and exponent sweep clocks are constants. The gather scans
one physical RAM word, and the terminal call uses its own evaluator clock. 

### `gather`

 Gathered word reports carry the actual source reads in their native
order. This bound also covers empty lists of words. 

### `jump`

 The singleton physical report for the first-tail or last-group router's choice of endpoint
write or configuration gather. 

### `same_logs`

 Private-clock independence for two complete executions on the same
choice words. Only the bound on each microcall changes. 

### `advice`

 The actual deterministic four-stage advice prefix is charged at its
four distinct tariffs. Its private work is bounded at the short native clock. 

### `AdviceExecution`

 A four-stage prefix on the exact distributed advice tape. 

### `AdviceExecution.memory`

 The physical memory at entry to the advice prefix-length stage, holding the copied
  distributed advice bits. 

### `AdviceExecution.values`

 The word-sized ordinals published by the advice layout for the evaluator's label order. 

### `AdviceExecution.count`

 The length of the distributed advice bit string copied into the physical preparation
  buffer. 

### `AdviceExecution.padding`

 The padding length in the serialized advice distribution after accounting for the raw
  prefix and ordinal data. 

### `AdviceExecution.bits`

 The actual copied bits whose sequence encodes the raw advice, ordinal map, and padding. 

### `InputExecution`

 The published permutation, physical middle exponents and blank tape
of the nonempty first tail group. The suffix starts exactly in the memory
returned by the preceding four advice stages. 

### `InputExecution.perm`

 The published permutation from physical dense labels to formal evaluator labels. 

### `InputExecution.dense`

 The exponent words in physical order on the incoming midpoint cut. 

### `InputExecution.formal`

 The exponent words in formal label order, related to the dense input by the published
  permutation. 

### `input_resources`

 Invoke the three linked tables at their actual addresses. The short
clock gives the private instruction bound even when the caller replays the
same advice and choices at a larger group clock. 

### `Incoming`

 Report shapes produced by the first-tail router and its native
deterministic prefix, before the last-group router. 

### `Outgoing`

 The last-group router selects either the gathered successor or its
accepting control-word sentinel. 

### `tail_resources`

 Total and per-call bounds for an actual native tail suffix, including
both router transfers and the successful terminal transition. 
