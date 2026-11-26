---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Algorithm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Algorithm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Algorithm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable separated arithmetic kernels

The arithmetic expressions and their postfix compiler in this file are data.
The evaluator contains no choice, no decision of a semantic proposition, and no
enumeration of the Cartesian product of the two inner lists.  Its instruction
counts are proved by actual transition traces.  An arithmetic instruction is
not a primitive bit-machine instruction: refining the supplied coefficient
operations to the latter remains a separate obligation.


### `Expr`

 Finite syntax for computations in the retained coefficient algebra. 

### `eval`

 Structural evaluation using the supplied, executable coefficient operations. 

### `size`

 Number of postfix instructions, including explicit coefficient loads. 

### `sum`

 A finite summation program. Its syntax contains each input exactly once. 

### `product`

 A finite group product; all factor computations remain explicit syntax. 

### `pow`

 Multiplication by a natural power, built by a terminating finite loop. 

### `map`

 Change only coefficient representations, leaving the program unchanged. 

### `eval_map`

 A proved implementation of the two coefficient operations transports
expression correctness. This does not assume a runtime for that implementation. 

### `TableTerm`

 A single explicitly stored term of a factor table polynomial. The list
contains its argument expressions together with their natural exponents. 

### `tableExpression`

 Compile a factor from its finite coefficient table, without expanding a
full untruncated multivariate polynomial. The supplied operations can themselves
be the clipped coefficient-list operations. 

### `Instr`

 The three actual instructions of the arithmetic kernel. 

### `State`

 Explicit remaining code and an explicit operand stack. 

### `step`

 One arithmetic-machine transition. Malformed programs stop on underflow. 

### `OperationCosts`

 Proposed costs for the three concrete operations. They acquire a machine
interpretation only through a measured simulation of the corresponding step. 

### `compile`

 Postfix compilation is structural and contains no interpreter oracle. 

### `cost`

 The costs of the actually encountered operands, not worst-case guesses. 

### `compile_trace`

 Every compiled expression executes without underflow, including in a larger
program. The bound is an actual trace length, not an assigned cost annotation. 

### `run`

 A bounded executable run of the compiled code. Its fuel is derived from
the program syntax and the result contains the actual final machine state. 

### `execute`

 Extract the result of the actual bounded postfix-machine run. The default
branch makes the function total and is proved unreachable for compiled code. 

### `compile_costedTrace`

 Data-dependent operation costs are attached to the same actual execution. 

### `runs_target_of_local_simulation`

 An actual local bit-level implementation, when supplied, yields an actual
target execution. The local simulation premise cannot be replaced by a cost
annotation or by semantic equality of the final answers. 

### `compileMany`

 Execute every moment program in order. Each program is present exactly once. 

 ## Constructive output-sensitive monomial enumeration 

### `exponentList`

 Enumerate nonnegative exponent vectors by spending the remaining degree
budget. Unlike the coordinate-box construction, this visits no rejected vector. 

### `exponentListEquiv`

 The list implements the actual bounded-exponent type counted by stars and bars. 

### `exponentCalls`

 Recursive invocations made by the budget-spending enumeration. This counts
invocations, not list-cell or bit operations. 

### `exponentListWithCalls`

 The executable enumerator with its recursive-invocation count attached. 

### `exponentCalls_le`

 The recursive search tree has at most D+1 invocations per output vector;
in particular the enumerator does not hide a full coordinate-box search. 

### `retainedSlots`

 The complete retained coefficient slots, with a concrete finite order. 

 ## Concrete dense coefficients and the arithmetic-machine backend 

### `Dense`

 A coefficient list with the fixed length of the retained-slot list. 

### `ofRaw`

 Projection is executable, and proves the fixed-length storage invariant. 

### `costs`

 These are exact counts of the instrumented coefficient-list operations,
and a list-cell load count. They are not primitive bit-operation counts. 

### `eval_dense_denote`

 Executing the real dense-list operations computes the canonical truncation
of the full polynomial expression. No full polynomial is built by the execution. 

 ## Finite coefficient extraction after moment execution 

### `collectCoefficientsWithCost`

 Sum explicitly requested coefficients. Each requested index is scanned by
the executable backend, and the counter also charges the final scalar addition. 

### `collapseU`

 Summing the retained U coefficients is performed after selecting X^a. 

### `finishAtWithCost`

 One output Z coefficient, accumulated over all supplied moment results. 

### `finishMomentsWithCost`

 The final jet is a list of its first D coefficients. All loops are finite;
the accompanying count includes coefficient scans and scalar accumulation. 

### `executeMoments`

 Execute each selected moment exactly once, then extract its coefficient
contributions. The list of moment indices is the constructive weak-composition
enumeration proved above. 

### `executeJet_finishing_cost`

 The finishing counter is polynomial in D times the moment count times the
retained coefficient-list length. It does not enumerate input assignments. 

### `extractPolynomial`

 Semantic version of coefficient extraction, used only to state correctness. 

### `collapseU_eq_extract_of_canonical`

 The executable scan is precisely extraction of X^a followed by U=1 on a
canonical representative. The order of these operations is explicit. 

### `executeRawJet`

 Fully executable polynomial-expression-to-jet code. Its input is finite
coefficient syntax for each requested moment, not a count or satisfiability oracle. 

### `executeRawJet_eq`

 The concrete jet code implements the canonical symbolic moment formula.
Identifying the supplied moment programs with the layout's grouped factors is
the subsequent mathematical integration step, not part of this hypothesis. 

### `WeightedTerm`

 One weighted group evaluation. The group itself is executable syntax,
so its computation cost is included rather than assumed to be one operation. 

### `Block`

 The two separate inner lists for one fixed choice of outer data. 

### `ofFunctions`

 Assemble one separated block from explicit inner enumeration lists. The
functions supply finite syntax for group computations, not their truth values. 

### `expression`

 The implementation of the product of the two independent sums in (4.8). 

### `expression_size`

 Exact instruction count, with no product of the two inner-list lengths. 

### `ofFunctions_eval_finset`

 The finite-list program agrees with the finite-set separated sum. Nodup
certifies that each coset element is enumerated exactly once. 

### `block_eval_of_independent`

 The list implementation agrees with (4.8) for input-dependent group
programs whose denotations satisfy the actual independence hypotheses. 

### `momentExpression`

 One moment is the sum over all supplied outer-data blocks. 

### `momentExpression_size`

 Exact size of all arithmetic instructions in one separated moment. 

### `momentExpression_trace`

 The concrete compiled separated loop has an execution certificate at its
proved instruction bound. Coefficient arithmetic and loads are still macrosteps. 

### `rawMomentExpression`

 The source-code builder for a separated moment. A raw coefficient-list
zero is the empty list; no operations on full polynomials are executed. 

### `rawMomentValue`

 Denotation of the explicit input programs for one separated moment. 

### `executeSeparatedJet`

 The separated finite counting kernel: build two inner sums per outer datum,
execute each moment over actual dense coefficient lists, and extract the jet. 

### `executeSeparatedJet_eq`

 Correctness of the actual separated kernel relative to its explicit input
group programs. The RHS is the canonical-moment expression of (4.7)-(4.8). 

### `rawMomentExpression_dense_cost`

 The dense execution cost of a separated moment includes every group
instruction and only the sum of the two inner-list lengths. 
