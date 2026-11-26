---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ParameterOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ParameterOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ParameterOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Effective selection of fixed parameters

The searches below take supplied Boolean tests. `select` uses the executable
least-number search `Nat.find`; the existence proof is used only to prove
termination. Executability is relative to the supplied test until its own
computability has been established. The bounded scan gives a separate finite
execution and counts calls to the test, not bit operations or Turing-machine
transitions.

The power-threshold application discharges its existence hypothesis explicitly.
The manuscript's binomial-tail and sparsification tests require their own
mathematical eventual-validity theorems before using the generic interface.


### `scanFrom`

 A finite scan of the interval `[start, start + fuel)`, recording test calls. 

### `scanFrom_min`

 No smaller number in the scanned interval passes the test. 

### `scanFrom_calls_eq`

 A successful scan checks each integer through its returned witness once. 

### `select`

 Executable least-number search. Only the Boolean test is inspected at run time. 

### `select_finite_execution`

 The total search is witnessed by a bounded scan with at most `select + 1`
Boolean predicate evaluations. This is not a bit-complexity assertion. 

### `select_bounded_execution`

 Any successful upper bound permits an entirely bounded implementation of
the same least-number search; the exact number of predicate calls is recorded. 

### `exists_good_of_eventual`

 An eventual bound supplies termination without extracting that bound as data. 

### `selectEventually`

 Search using an eventual-validity proof. No classical choice is used. 

### `selectAtTop`

 Interface for asymptotic proofs stated using the natural-number `atTop` filter. 

### `select_congr`

 Tests defining the same admissible set give the same chosen constant,
regardless of the proofs used to certify termination. 

### `select_input_independent`

 If a test is independent of the input size, its least successful parameter
is independent too, even when the supplied existence proofs were indexed by it. 

### `parameterFamily`

 One effective choice for each width. There is deliberately no input-size
argument: only the width indexes the supplied Boolean test. 

### `large_prime_exists`

 Euclid's theorem supplies termination for a direct primality search.
The test itself is decidable natural arithmetic and primality. 

### `largePrime`

 The least prime at least three and at least the requested bound.
In particular, the manuscript can fix `largePrime (2 ^ 4096)` before reading
any formula. 

### `largePrime_log_bound`

 Fixing a prime above `2 ^ minBits` supplies the manuscript's required
Boolean chunk capacity without any dependence on the input size. 

### `power_threshold_eventual`

 A concrete eventual bound for the extension-size search. It uses
`m < p^m`, so `target` itself suffices as an exponent bound. 

### `powerExponent`

 Find an extension exponent whose number of nonzero field elements meets
an arbitrary prescribed natural-number threshold. 

### `and_eventual`

 Combining independently proved eventual requirements remains effective;
the maximum of their thresholds proves termination of the combined search. 

### `computable_select`

 A computable family of tests with a proof of pointwise success has a
computable least-witness function. The success proof is not a truth oracle. 

### `computable_parameterFamily`

 Width-indexed fixed parameters are a computable family when their
admissibility test is computable and the eventuality theorem is proved. 

### `primrec_power_test`

 The natural power-threshold predicate used above is primitive recursive. 

### `computable_powerExponent`

 For each fixed base at least two, the least successful extension exponent
is a computable function of the requested size threshold. 

### `largestProperDivisor`

 Bounded trial division, used to prove primality testing computable. 

### `primrec_prime`

 The manuscript's primality test has a primitive-recursive implementation. 

### `computable_largePrime`

 The prime is selected uniformly from the requested numerical lower bound. 
