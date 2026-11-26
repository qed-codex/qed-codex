---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/CountPrime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/CountPrime.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/CountPrime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The count for one prime (proof of Theorem 17, "Hashing modulo a prime")

"For every prime p in the range we count the triples with S(a,b,c) ≡ 0 (mod p)", where S(a,b,c) =
w(a,b) + w(b,c) + w(a,c) is the weight of the triangle.  "Let P[a,c] := x^{w(a,c) mod p} and Q[c,b]
:= x^{w(b,c) mod p} be matrices over the ring ℤ[x]/(x^p - 1) […]; then F(p) + Z₀ is the sum over the
pairs (a,b) ∈ A × B of the coefficient of x^{-w(a,b) mod p} in (PQ)[a,b]."  Here F(p) is the number
of triples with S(a,b,c) ≠ 0 and p ∣ S(a,b,c), and Z₀ the number of triples with S(a,b,c) = 0.

countPrime(n, ab, bc, ac, p, len, K, N2, w) computes this count for one prime, in a work area at w.
Two letters of the quotation mean something else in the code.  There w is the address of the work
area, and the weights are the three lists ab, bc and ac.  And `P` is the program, while the matrices
P and Q occur only as the lists `matPList` and `matQList`.

The routine has three parts.

* The addresses of the parts of the work area (`cpAddr_spec`); they lie one behind the other
  (`cp_places`).
* Six tables: the doubles of p, the residues of the three lists of weights, the places of the
  Z-order, and the sizes 4^i p of the matrices of Strassen's recursion, which szTable(dst, p, J)
  writes (`szTable_spec`, `cpTables_spec`, `CpTabs`).
* The matrices P and Q in Z-order, their product by Strassen's algorithm, and the sum of the
  coefficients (`cpProduct_spec`).

`countPrime_spec` puts the three parts together.


 ## The program 

### `CpNums`

 The numbers of the procedures that countPrime calls. 

### `CpCtx`

 The program holds the procedures that countPrime calls. 

### `Num`

 The local variables of countPrime.  The arguments n, ab, bc, ac, p, len, K, N2, w: N2 = 2^K is
the number of rows and columns of the padded matrices, and w, the address of the work area, is also
the address of the table of doubles.  Then n²; the addresses of the residues of the lists ab, bc and
ac, of the table of places and of the table of sizes; the size 4^K p of a matrix; the addresses
of P, Q, PQ and of the scratch space of Strassen's algorithm; a local that takes the results of the
calls, except the last one, whose result (the count) goes to local 0 and is returned. 

### `cpAddr`

 The first part of countPrime: the addresses of the parts of the work area. 

### `cpTables`

 The second part: the table of doubles, the residues of the three lists, the table of places, the
table of sizes. 

### `cpProduct`

 The third part: the matrices P and Q, their product, the count. 

### `countPrimeBody`

 countPrime(n, ab, bc, ac, p, len, K, N2, w). 

### `countCells`

 The number of cells of the work area of countPrime.  (The last summand is not written; it is
room that Strassen's algorithm asks for.) 

### `countTime`

 An upper bound on the number of steps of countPrime. 

 ## The layout of the work area 

### `cpRab`

 The address of the residues of the list ab. 

### `cpRbc`

 The address of the residues of the list bc. 

### `cpRac`

 The address of the residues of the list ac. 

### `cpMort`

 The address of the table of places. 

### `cpSzt`

 The address of the table of sizes. 

### `cpPm`

 The address of the matrix P. 

### `cpQm`

 The address of the matrix Q. 

### `cpRm`

 The address of the product. 

### `cpScr`

 The address of the scratch space of Strassen's algorithm. 

### `cp_places`

 The parts of the work area lie one behind the other; as one fact. 

### `cpFrame`

 The local variables of countPrime after its first part. 

### `cpAddr_spec`

 **The first part of countPrime**, in 50 steps. 

 ## What countPrime assumes 

### `CountPrimePre`

 What countPrime needs: the three lists of n² weights of absolute value at most U < 2^len lie
below the work area, the work area lies in the memory, and the numbers that are formed fit in a
word. 

### `length_residList`

 A list of residues is as long as the list of numbers. 

### `lt_of_mem_residList`

 Residues modulo p are below p. 

### `CountPrimePre.four_le_word`

 The constant 4 fits in a word. 

### `CountPrimePre.size_le_word`

 The size of a matrix fits in a word. 

### `CountPrimePre.sq_le_word`

 The number of entries of a matrix fits in a word. 

### `CountPrimePre.dbl_le_word`

 The entries of the table of doubles fit in a word. 

 ## The procedures that countPrime calls 

### `dblTable_meets`

 **dblTable** as a procedure. 

### `residues_meets`

 **residues** as a procedure. 

 ## The tables 

### `CpTabs`

 The tables of countPrime are in their places. 

### `CpTabs.keep`

 The tables stay in their places when only cells behind them change. 

### `CountPrimePre.residuesPre`

 What a call of residues from countPrime assumes: the list l of weights at src lies below the
work area, the table of doubles is written, and the residues go to dst, behind that table. 

### `cpTables_spec`

 **The second part of countPrime** writes the six tables. 

 ## The product and the count 

### `CountPrimePre.buildZPre`

 What a call of buildZ from countPrime assumes: the residues R stand at r, one of the three lists
of residues, and the matrix goes to dst, behind the tables. 

### `cpProduct_spec`

 **The third part of countPrime** returns the count. 

### `countPrime_spec`

 **countPrime** returns the count of the proof of Theorem 17 for the prime p, and changes only
cells of its work area. 

### `countPrime_meets`

 **countPrime** as a procedure. 

 ## Larger primes need more cells and more time 

### `countCells_mono`

 The work area grows with p. 

### `countTime_mono`

 The time grows with p. 
