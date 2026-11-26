---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSymbolicCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSymbolicCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSymbolicCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform symbolic list costs for growing parameters

The old canonical-list algorithm has an explicit fixed-degree event bound. This
module retains its interfaces and makes all parameter dependence visible. It also
refines exponent addition to an actual unary bit-string algorithm. Unary is used
only for exponent indices, whose values are O(D), never for ring coefficients.

Counters below are charged operations/bit inspections. A primitive tape-machine
execution certificate is a separate requirement.


### `coefficientBits`

 Ring coefficients have h base-ring coordinates, each with at most (D+1)b bits.
Here b is a supplied upper bound on log₂ p; no fixed-parameter constant is hidden. 

### `listFactor`

 Exact fixed-degree polynomial multiplier of M_X^4 in the actual old
instrumented list algorithm. It does not depend on k, p, or h. 

### `parameterSize`

 A single size variable for displaying absolute polynomial degrees. 

### `retained_index_bits`

 Uniform input/output key size; coefficients are not encoded in unary. 

### `weighted_dense_events_uniform`

 The weight q is an independently verified per-event realization bound.
This arithmetic consequence alone is not a machine-runtime theorem. 

### `weighted_dense_events_degree`

 Absolute degree accounting once an independently realized event cost has
been bounded. This does not manufacture that realization certificate. 

### `addIndexBits`

 Add two unary-delimited sequences directly, copying true bits from each
current number, then consuming both false delimiters. Each transition inspects
at most two bits and writes at most one bit; the counter charges three events. 

### `addIndexBits_prefix`

 The two current unary numbers are added without converting them to Nat. 

### `addIndexBits_words`

 Correctness for equal-length coordinate arrays. 

### `addIndexBits_cost`

 Every recursive call consumes at least one actual input bit. 

### `fixedKey`

 Fixed-width framing for record scans. Padding is outside the D+2 unary
numbers, so reading exactly those D+2 numbers recovers the original key. 

### `keyBlockCode`

 A computable fixed-width record key, ready for BitProgram scans. 

### `recordBlockCode`

 Fixed-width key/payload records, with the key at the head of the stream. 

### `framedRecord`

 Escape framing makes record boundaries explicit to finite-control scans. 

### `ingestLiteral`

 Loading a raw literal really runs projection and pays for all source terms. 

### `ingestLiterals`

 Explicit ingestion of all raw literals supplied to an expression compiler. 

### `storedBits`

 Actual serialized key and coefficient payload length. Delimiters for the
key are included; any outer list-cell encoding overhead must still be added. 

### `baseEventBudget`

 A single explicit bound for both implemented binary base-residue operations.
The coefficient capacity is B=(D+1)b bits and the modulus may use one extra bit. 

### `baseEventBudget_degree`

 The exponent four is absolute; it does not depend on p, h, D, or k. 

### `quartic_mul_events`

 This bounds the already implemented binary quartet multiplication,
including its Horner reduction. There is no abstract scalar multiplication
hidden in this particular counter. 

### `lambda_storedBits_bound`

 Instantiate the storage bound with the actual injective prime-power
extension-ring encoding. Its construction/evaluation cost is separate. 

### `coefficientBlockCode`

 The already proved quotient encoding, now packaged for record scanning. 

### `RepresentedRing`

 An actual coefficient implementation with a semantic decoder. No ring laws
are postulated on code words. Each operation returns its own measured counter. 

### `ScalarBudget`

 Independent per-call bounds for the concrete scalar routines. 

### `RingProgram`

 Executable callbacks only. The semantic decoder is deliberately absent. 

### `QuarticCode`

 Actual coefficient data: four fixed-width binary words. 

### `preparedProgram`

 Repeated arithmetic uses only supplied modulus, reduction, and constant
caches. Returning a cached constant charges no scalar arithmetic; a concrete
stack implementation must additionally charge copying its bits. 

### `preparedRing`

 The semantic certificate is separate from the executable program. 

### `ProgramBudget`

 Bounds on executable callbacks require no decoder or algebraic laws. 

### `bitScan`

 Equality reads the actual requested and stored key bits. 

### `bitRow`

 Product exponents are formed by the direct bit-string adder. 

### `bitEventFactor_degree`

 An absolute polynomial, including concrete binary coefficient arithmetic
and bitwise exponent comparisons/additions. List administration still uses
source events; this is not a primitive-machine trace theorem. 

### `preparedProgram_budget`

 The cost bound depends only on the actual callbacks. In particular it
does not need any semantic hypothesis on the cached reduction or constants. 

### `QuarticInitialization`

 Data retained between calls to the scalar binary routines. 

### `initializeQuartic`

 Setup uses binary multiplication for the prime power, binary negation for
the reduction data, and explicit bit copying/padding for the two constants. 

### `wordBlockCode`

 Fixed-width words are already their own executable bit representation. 

### `quarticCodeBlockCode`

 The actual raw coefficient payload has exactly four binary words. 

### `RepresentedRing.map`

 Postcompose only the mathematical decoder. Every executable callback,
including its returned cost, remains literally unchanged. 
