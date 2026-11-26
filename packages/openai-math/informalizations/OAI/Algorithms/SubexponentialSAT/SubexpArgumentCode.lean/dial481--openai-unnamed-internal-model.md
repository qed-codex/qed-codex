---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpArgumentCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpArgumentCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpArgumentCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable raw coefficient lists for marked incidence arguments

The executable definitions consume only a scalar beta and finite Taylor
coefficient arrays. They construct lists of explicit exponent indices and
scalars; no `Polynomial` occurs in an executable definition.


### `constantIndex`

 An index with no input-coordinate variables. 

### `coordinateIndex`

 The index of U^u Z^z X_i, represented by an actual finite coordinate function. 

### `rawRow`

 Emit one coefficient-list entry for each coordinate of one linear row. 

### `compileArgument`

 Compile beta + U(row_0 X - beta) + sum_{1<=j<=r} Z^j row_j X.
Zero coefficients are deliberately retained; no equality test on A is needed. 

### `coefficientAt`

 Zero-extension of the supplied finite coefficient array. 

### `collectRowsWithCost`

 Execute each row compiler once and append its output, counting actual
copied cells and one loop event for each row. 

### `compileArgumentWithCost_eq`

 Exact count of the declared construction events, alongside the actual output. 

### `semanticRow`

 Mathematical meaning of a row from the finite Taylor array. 

### `sum_positive`

 Reindex the positive Taylor coefficients without introducing a polynomial oracle. 

### `denote_compileArgument`

 Denotation of the literal compiler is exactly the marked incidence argument. 

### `denote_compileArgument_eq_rowArgument`

 Connect an executable finite Taylor array to the existing row-path argument.
The equality hypothesis only identifies the input scalar array; the literal
compiler itself never reads a mathematical polynomial. 

### `ingest_compileArgument_cost`

 The existing literal-loader bound now applies to this concrete compiler. 
