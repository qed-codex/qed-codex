---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HeckeFunctionalEquationAbs.lean",
  "declarations": [
    "GlobalTheory.Published.HeckeFunctionalEquationAbs"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Seven additional assumptions for the maximal slope bound

[Definition / hypothesis ARAK.D087](https://andrewodesky.com/rh/lean/GlobalTheory.Published.HeckeFunctionalEquationAbs/)

The following seven statements are assumed in "A maximal slope bound at points admitting compatible choices". Conditions marked not expanded are part of the assumptions; their meaning is not inferred from their names.

**(1) Functional equation.** For every totally complex number field $E$, finite set $I$ with maps $\phi_i:E\to\mathbb C$ such that every embedding of $E$ is uniquely $\phi_i$ or its complex conjugate, unitary Hecke character $\chi$, integers $n_i$ not all zero, and finitely supported exponents $a_v\in\mathbb N$, suppose the infinity type and local exponent conditions hold and $\Lambda,\Lambda'$ satisfy the completed-function conditions for $(\chi,n)$ and $(\chi^{-1},-n)$. Then there is $|\epsilon|=1$ such that, for all $s\in\mathbb C$, $$\Lambda(s)=\epsilon\left(|\operatorname{disc}E|\prod_v (\mathrm N v)^{a_v}\right)^{1/2-s}\Lambda'(1-s).$$ Each completed-function condition requires an entire function equal on $\operatorname{Re}s>1$ to a specified archimedean factor times the Euler product. The infinity type, exponents and the factors are not expanded.

**(2) Valuation bounds.** For every abelian CM field $E/\mathbb Q$, natural number $d$, finite family of embeddings $\phi$, and $s\ge1$ satisfying a field-data condition, there are rational numbers $z_C$ indexed by ideal classes, represented as values at $1-2s$ of functions satisfying a class-zeta condition. For every weight, ideal, period pair and Hecke character satisfying the stated base, lattice and character conditions, and every prime $\ell$ and finite set of places satisfying the stated splitting and coprimality conditions, a specified lower $\ell$-adic valuation bound holds both for each specified class term and for each specified toric sum twisted by a character of the relevant ideal class group. The field-data, class-zeta, terms, normalization and valuation bound are not expanded.

**(3) Transport of periods and sums.** For every quadratic number field $K$ of discriminant $-d$, $d>4$, embedding into $\mathbb C$, and period pair satisfying a lattice condition, there are, for each automorphism of $\mathbb C$, a finite idele, fractional ideal and period pair. For automorphisms fixing the embedded $K$ they satisfy two lattice conditions and an equality of $j$-values; the ideals satisfy an equidistribution condition. For every CM field $E$ Galois over $\mathbb Q$, containing $K$ satisfying a finite-place condition (not expanded), with at least two embeddings extending the chosen embedding, and for every positive integer $s$, positive weights and base ideal satisfying the relevant conditions, a further assertion holds: specified normalized sums are algebraic and have specified conjugation and absolute-value formulas, and ratios of two specified sums with nonzero denominator are algebraic and have a specified conjugation formula with nonzero conjugate denominator. The lattice, equidistribution, sum and normalization conditions and the formulas are not expanded.

**(4) Transport of twisted sums.** For every quadratic number field $K$, $d>0$, $\delta\in K$ with $\delta^2=-d$ and embedding $K\to\mathbb C$, there is a nonzero complex period $\Omega_0$. For all specified CM extensions, embedding families, weights, ideals, finite sets, characters and twisted sums satisfying a datum condition, a specified normalized sum using $\Omega_0$ is algebraic over $\mathbb Q$. For every compatible algebraic closure, embedding and global Artin map, and every compatible complex automorphism, Galois element and finite idele, there is another nonzero period $\Omega_1$ such that all corresponding conjugate twisted sums obey the stated transformation formula. The datum, normalized sums, compatibility conditions and transformation factors are not expanded.

**(5) Denominators of partial zeta values.** Let $E$ be a CM field, $F$ its maximal real subfield, $r=[F:\mathbb Q]$, $k=2s$ with $s\ge1$. There are rational numbers $z_C$ indexed by ideal classes $C$ of $F$ such that each $z_C$ is the value at $1-k$ of a complex function differentiable away from $1$ and equal to $\sum_{I\in C}(\mathrm NI)^{-z}$ for $\operatorname{Re}z>1$, the sum running over nonzero integral ideals in $C$.

For every such family $z_C$ define $c_\ell=\max_C\max(0,-v_\ell(z_C/2^r))$ and $m_\ell(n)=\inf\{v_\ell(a^n-1):a\ge2,\ (a,\ell)=1\}$. For every prime $\ell$, $$c_\ell\le r\,v_\ell(2)+m_\ell(rk),\qquad m_\ell(rk)=\begin{cases}0&\ell\ne2,\ \ell-1\nmid rk,\\1+v_\ell(rk)&\ell\ne2,\ \ell-1\mid rk,\\2+v_2(rk)&\ell=2.\end{cases}$$ If $rk\ge16$, only finitely many $c_\ell\log\ell$ are nonzero and $\sum_\ell c_\ell\log\ell\le rk\log(rk+1)$.

**(6) Reflection relation.** For all records satisfying a condition (not expanded), for every choice satisfying another condition (not expanded), every pair of indices $i,j$, every parameter $t$, and functions $\Lambda,\Lambda_0$ satisfying the respective Hecke-function conditions (not expanded), if $1-e_{ij}\le s\le0$ is an integer, there is a coefficient $u$ in the record's number field with $$\Lambda(s)\Lambda_0(1-s)=u\,\Lambda(1-s)\Lambda_0(s).$$ There are an algebraic integer $a$ and $k,k'\in\mathbb N$ such that $a\mid Q^ {k'}$ and $uQ^k=a$, where $Q$ is a natural number attached to the record (not expanded). The integers $e_{ij}$ and the functions' parameters are not expanded.

**(7) Separating functionals.** For every real $\varepsilon$ and $C_F\ge6510$ there is $x_0$ such that, for all size data of parameter $\varepsilon$ and $x\ge x_0$ satisfying two conditions, and all finite groups, families and realisation records satisfying the stated conditions, the following holds for every compatible grid, Weil datum and row volume: for every nonzero vector $w$ in a specified space, there are a real vector $\rho$ and a complex linear functional $\xi$ such that, for every nonzero $t$ in a specified set, some column $\Psi$ and datum $\Phi$ satisfy a convergence condition and a specified value depending on $w,t,\rho,\xi,\Psi,\Phi$ is nonzero. The objects, compatibility, convergence and value are not expanded.
