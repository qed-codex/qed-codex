---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed-size, executable quartic ring implementation

The data are four coefficients.  Multiplication is Horner evaluation with
the explicit reduction `T^4 = t0 + t1*T + t2*T^2 + t3*T^3`.
The coefficient operations are parameters of the implementation; the binary
instance below discharges their correctness and uniform finite-event bound.


### `shift`

 One multiplication by the root, followed by the fixed quartic reduction. 

 These loops execute exactly the displayed scalar calls. 

### `Word`

 The type stores the width invariant; its alphabet remains `Bool`. 

### `wordNeg`

 Canonicalize once, then execute the verified bitwise modular negation.
This operation accepts every width-correct input, including unreduced words. 

### `binaryMul`

 Actual binary quartic multiplication. Every output word has the same
width as the input words, including all intermediate coefficient words. 

### `binaryMul_cost`

 Forty-nine calls to concrete quadratic-cost binary scalar programs.
This is a source-event budget, not a machine simulation theorem. 

### `reductionData`

 The four reduction coefficients are the negatives of the four stored
coefficients of the monic defining polynomial. 

### `reductionWords`

 Only the four supplied coefficients are stored; selection of the
defining polynomial is supplied by `QuarticSearch.liftedCoefficients`. 

### `binaryMul_quotient`

 This is refinement into the exact polynomial quotient whose coefficients
are input data, rather than a separate existentially chosen isomorphic field. 
