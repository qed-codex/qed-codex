---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Closed fixed-bit F₃ factor checker. The complete command is independent
of the degree. All coefficient addresses and loop bounds are runtime unary
words; source vectors are preserved and scratch stacks are discharged. 

 Coefficient 

 A fixed coefficient kernel: two preserved source arrays, a preserved
unary coefficient address plus one, and an output stack. Every copy, padded
prefix, coefficient reversal, multiply-add and cleanup is an actual call. 

 CoefficientRun 

 The closed, fixed-program boundary for one arbitrary convolution
coefficient. Its sources and runtime unary address are preserved and all
work stacks are empty again. 

 ProductLift 

 A framed invocation of the source-preserving coefficient kernel. The
extra stack stores the remaining runtime product length. 

 Product 

 A fixed outer loop runs the coefficient kernel at successively longer
unary addresses. Source arrays are preserved; all output coefficients are
physically written in decreasing degree order. 

 ProductRun 

 Monic 

 Appending the implicit monic coefficient uses two physical transfers.
No input-dependent instruction table or uncharged array append is used. 

 MonicAlgebra 

 CheckLift 

 Framed calls to the physical Boolean predicates. 

 PairProduct 

 Candidate 

 ProductCheck 

 Pair 

 Closed primitive pair test. All three source vectors and the runtime
unary degree are preserved. The return bit is exactly the scalar pairPass. 
