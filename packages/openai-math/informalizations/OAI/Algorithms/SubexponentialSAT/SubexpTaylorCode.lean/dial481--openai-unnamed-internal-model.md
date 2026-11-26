---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTaylorCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable Taylor coefficient caches for incidence-argument compilation

Input paths are dense coefficient lists. Each path is shifted once by the
existing Horner loop, then its first q+1 coefficients are read into a real
array cache. Mathematical polynomials occur only in semantic theorems.


### `readWithCost`

 A zero-default coefficient read, charging every visited list cell and
its terminal check. It has the same value as `List.getD`. 

### `buildRow`

 The shifted list is bound once; every lookup result is cached once. 

### `buildTaylor`

 Each coordinate's dense path is shifted once before its finite row is
stored. Later consumers read the stored arrays rather than shifting again. 

### `coefficients`

 Finite Taylor array in the orientation consumed by `compileArgument`. 

### `compileDenseArgument`

 Direct dense-path-to-raw-incidence compiler. 

### `compileCodeWithCost`

 Compile the actual finite expression tree to a dense coefficient list.
Recursive outputs are shared with the instrumented arithmetic operations. 

### `codeWeight`

 A scalar-independent size of the finite expression; X receives weight two
because its dense list stores both its constant and linear coefficient. 

### `codeLengthBound`

 A sharper bound for stored list length: addition takes a maximum. 

### `buildCodeTaylor`

 Compile every coordinate once, then shift and cache its coefficients once.
The compiled lists are stored before either their values or costs are read. 

### `compileCodeArgument`

 Complete expression-path-to-raw-incidence compiler. 

### `ArgumentResult`

 Costs remain in their declared units: coefficient-ring arithmetic,
coefficient-list visits, and raw-emitter construction events. 

### `compileCodeArgumentWithCost`

 Instrumented complete frontend, sharing both the cache and raw emitter. 

### `compile_mismatchRowCode_length`

 Dense output length for the actual row-expression constructor, including
any trailing zero padding introduced by the schoolbook arithmetic. 

### `coefficients_buildTaylor`

 Every stored scalar is the coefficient of the actual shifted polynomial. 

### `denote_compile_mismatchArgument`

 End-to-end specialization to the generated interpolation expressions. 
