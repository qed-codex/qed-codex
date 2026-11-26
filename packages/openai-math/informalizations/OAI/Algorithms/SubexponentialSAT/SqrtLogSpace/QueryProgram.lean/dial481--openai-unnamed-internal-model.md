---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete bit primitives for streamed finite-difference queries. 

### `parityProgram`

 Scan the actual bits, accumulating their XOR in register 2. 

### `parity_sign`

 The sign is determined by the number of true bits, not the length or
numeric value of the binary word. 

### `parity_prefix_space`

 This scan is a polynomial-time local routine, so its complete local
prefix storage follows from the actual trace budget. 

### `pairSign`

 Finite table for the sign of a streamed pair. Both masks are preserved;
only one scan buffer and one copy temporary are needed. 

### `pairSign_correct`

 Subset pairs have the finite-difference sign even though the machine only
computes XOR and never subtracts an unbounded integer. 

### `pairSign_prefix_space`

 All prefixes of the fixed pair-sign program use polynomial local space.
This bound includes the preserved masks and both temporary stacks. 

### `pairRegisters`

 Shared leaf ABI for pair signs: preserve both masks and every suspended
signature frame, with output848 and a single scratch word849. 

### `scalePorts`

 The forty arithmetic ports are disjoint from the preserved sign bit. 

### `signedScale`

 A positive sign transfers unchanged bytes; a negative sign invokes the
original actual ternary scalar multiplier with its cached negative unit. 

### `signedScale_eval`

 The sign branch executes a fixed native program; readiness consists only
of the concrete scalar-ring data and bounded empty-support input dictionary. 

### `leafArithmeticRegs`

 Physical arithmetic registers lie below the four suspended DFS flags. 

### `leafScalePorts`

 Consume the current pair array on 851; the sign remains on 848. 

### `leafNormalizePorts`

 Share the existing scalar parameters, consume scaled output 38, and
normalize into node accumulator 850. All other arithmetic scratch is below128. 

### `signedAccumulate`

 One actual signed finite-difference term is added to the retained node
array. Neither call constructs a support family or an assignment product. 

### `ScaleReady`

 Concrete port readiness for the signed scaler. This is a physical input
condition for this local instruction sequence, not an evaluation service. 

### `NormalizeScratchReady`

 Only the normalizer's peripheral scratch must be empty. Its parameters
are shared with the actual scalar machine. 

### `signedSum`

 The normalized result is an exact signed addition in the retained array. 

### `signedAccumulate_eval`

 Both arithmetic branches and the additive normalization execute on one
fixed physical command. The initial hypotheses describe its actual input words. 

### `signedAccumulate_run_space`

 The compiled signed addition has a polynomial bound at every local source
prefix, measured from all caller stacks, including persistent query state. 

### `pairUpdate`

 Update the node accumulator for a completed pair and clear its sign cell
before the next pair. The pair masks themselves are read and restored. 

### `pairUpdate_eval`

 Exact actual signed update, including mask scans and sign cleanup. 

### `pairUpdate_run_space`

 The mask scan, signed update and cleanup share this same compiled run. 

### `pairUpdateResult_frame`

 Exact stack framing of the complete pair arithmetic: only node850 and
consumed pair851 differ from the input state. In particular E/U, all suspended
representatives, and every loader/cache master survive. 

### `pair_signedSum_dense`

 The actual Boolean parity used by the program is the exact
finite-difference sign, including the empty support. 
