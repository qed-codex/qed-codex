---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpProgramBuilder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProgramBuilder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProgramBuilder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the separated program from finite coefficient data

The input consists of finite factor tables, residue rows, Taylor coefficient
arrays, support lists, outer base points, and individual color increments.
Every factor argument and every weight is computed from these data. No field
of the input contains a correct answer or a ready-made group expression.

The only enumeration of assignments is an outer list followed by one separate
inner list for each color. The Cartesian product of inner lists is never
constructed. The bounds keep the number of colors, table rows, variables,
factors, and interpolation coefficients visible.


### `FactorData`

 Stored data for one factor at one interpolation node. `origin` is over the
residue field; `taylor` stores the coefficients of each shifted row path. 

### `argument`

 Compute the lifted original linear form, then emit the marked Taylor
argument as a finite raw coefficient list. 

### `factorExpr`

 Tensor interpolation is evaluated in factored Horner form. Each input
literal is the explicit argument above, not a polynomial-valued oracle. 

### `groupExpr`

 Only the factors assigned to this color are multiplied. 

### `shifted`

 Addition happens in the residue field before applying the chosen lift. 

### `executeJet`

 The complete coefficient-list jet algorithm generated from stored input
data. In particular, group expressions are built inside this definition. 
