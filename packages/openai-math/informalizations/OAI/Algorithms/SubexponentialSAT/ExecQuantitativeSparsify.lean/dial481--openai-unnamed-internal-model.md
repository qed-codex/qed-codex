---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecQuantitativeSparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecQuantitativeSparsify.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecQuantitativeSparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantitative bounds for the executable list sparsifier

This module instantiates the actual list search and depth-first worklist at the
arithmetically selected inverse budget. The finite-set view of each output is
used only for SAT semantics. Node visits are counted by the actual worklist;
they are not presented as primitive bit-machine transitions.


### `literalList`

 The fixed syntactic order on the literals of a clause. 

### `orderedClauses`

 The fixed syntactic order on clauses, independent of their truth values. 

### `formulaList`

 A concrete list representation of the typed input formula. 

### `formulaList_codes`

 The numerical payload of the executable input is exactly the canonical
payload specified by `Encoding`, including both sorting conventions. 

### `encodedLiteral_length_le`

 The actual unary literal representation is bounded by the ambient variable
count; literal comparisons are not treated as constant-size operations. 

### `encodeRawFormula_polynomial`

 Each normalized intermediate formula has polynomially many bits. The
displayed coefficient and degree depend only on the fixed clause width. 

### `executeFor`

 Execute the list algorithm at the explicit threshold parameter. 

### `leavesFor`

 The output in the finite-set SAT interface, obtained from actual raw output. 

### `chosenLeaves`

 Actual executable-list leaves at inverse budget s. 

### `chosenExecute_visits_polynomial`

 A uniform polynomial factor for the actual number of worklist visits.
The counted transition invokes the explicitly defined list search; a further
bit-program refinement must charge the operations inside that search. 

### `sigmaExecute`

 The rational interface first rounds the reciprocal budget; it never
raises numbers to powers proportional to an unreduced input denominator. 

### `sigmaLeaves_spec`

 The finite-output and incidence conclusions of quantitative sparsification
for every rational budget. The constants precede the budget and the input.
Primitive bit-runtime is a separate refinement obligation. 
