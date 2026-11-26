---
{
  "module": "OAI/Computability/VPVNP/CompressorChoiceRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native RAM admission for a compressor motif

Appendix E scans the outer indices of Theorem 6.1 in supply-edge order. This
finite instruction table reads each coordinate as a full machine word, checks
its cap, stores the payload, and accumulates the cleared quadratic score. Both
valid and rejected prefixes can be embedded in larger native programs. For a
complete call the successful streams are exactly the encodings admitted by
the motif inequality. The complete call reads the repetition count from persistent state and
computes its cap and energy limit using fixed motif coefficients.


### `low`

 Registers 0–2 implement the word reader, register 3 holds the exclusive
coordinate cap, register 4 the running energy, and register 5 the exclusive
energy limit. The following registers retain the complete guessed vector. 

### `slot`

 Register retaining guessed supply coordinate `i`, after the six reader and score registers. 

### `coordinate`

 The public datum at a coordinate is its fixed cleared quadratic coefficient.
Only the three numerical bounds/counters in the incoming registers depend on the call. 

### `scan`

 The final comparison is performed even when the supply arity is zero. 

### `coordinate_prefix`

 A successful coordinate choice executes the native eight-label word reader
and six deterministic instructions. The coordinate slot is retained for the descriptor. 

### `encoding`

 Full-word choices in the prescribed order of the descriptor scan. 

### `score`

 Energy is accumulated over the coordinates actually visited by the scan. 

### `scan_prefix`

 The accepting prefix uses one final guard and `4*w+10` native steps per
coordinate, and every visited slot holds exactly its encoded coordinate. 

### `coordinate_reject`

 An out-of-range coordinate transfers to the actual rejecting continuation
immediately after the word read and its guard, before performing arithmetic. 

### `scan_reject`

 A rejected candidate reaches the rejecting label on a prefix of its encoding.
For candidates outside the coordinate box no fit assumption on their score is required. 

### `scan_sound`

 Every successful machine stream consists of complete words, has exactly the
prescribed length, and passes both numerical tests. The fit condition covers the entire
box so that an overweight candidate cannot gain admission by wrapping around. 

### `scan_execute_iff`

 Complete calls of the linked native scan are exactly the canonical encodings
of admitted vectors. Extra or truncated streams fail, including at zero supply arity. 

### `prefix_probes`

 The native prefix consists entirely of private ticks and binary choices. 

### `full_encoding`

 With supply slots in numerical order the scan consumes the concatenation
of the little-endian word representations, including leading zero bits. 

### `full_score`

 The public quadratic coefficients include the squared radius denominator;
the accumulator therefore computes the complete left side of the admission test. 

### `scan_admit_iff`

 With positive supply masses and representable bounds, acceptance of the actual
machine agrees with the integer admission test used in the outer sum of Theorem 6.1. 

### `unitSlots`

 The unit term has no payload. Write the zero descriptor without guessing
bits, even when the incoming register file still holds the preceding motif. 

### `choosePayload`

 The repetition count arrives in scratch register two, and the energy
accumulator in register four starts at zero. Both branches have fixed code. 

### `choosePayload_execute_iff`

 The native call's complete streams are exactly those of the outer-index
reader, including the unit branch. All bound checks take place on machine
words whose exact numerical contents are given by the register hypotheses. 

### `native_word_fit`

 For fixed rational motif data a constant plus twice the binary logarithm of
`M+1` suffices for the entire native reader. This covers the one-past guards,
all public weights, and the largest energy considered in the overflow proof. 

### `scaleDigits`

 Multiply by a coefficient built into the fixed instruction table in binary.
The source survives, and the destination is initialized afresh. 

### `scaleFixed`

 Encode fixed motif coefficients in the code, independently of the actual
machine word width or the length-dependent public data. 

### `prepareBounds`

 The input repetition word is register 2. The code sets register 3 to one
past the coordinate cap, register 5 to one past the energy limit, and clears
the scratch and energy registers before dispatching on the repetition word. 

### `prepareBounds_length`

 Constant instruction cost for a fixed motif. Only the binary lengths of the
fixed coefficients enter the bound, independently of the word size and of `u`. 

### `prepareBounds_exec`

 Exact register effects at the continuation of threshold preparation. The
hypotheses concern only the two final natural bounds, since the intermediate
word computations agree with the integer expressions modulo the word modulus. 

### `prepareBounds_execute`

 Linked native execution of the preparation table reaches the choice block
with the exact cap and limit, without consuming a branch bit or making a probe. 

### `choiceCall`

 The compiled call enters with the repetition count as its persistent word.
All private registers and memory start with the usual machine reset. 

### `compiled_outer_choices`

 At every sufficiently wide word size the same fixed instruction table has
one successful stream per admitted outer index. This call begins at the native
machine entry point and includes all threshold preparation. 
