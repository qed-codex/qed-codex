---
{
  "module": "src/Formalism/LocalToGlobal/NormalizedHeckeFactors/RingHomOfBaseOrderToFraction.lean",
  "declarations": [
    "Formalism.L2.NExpTied",
    "Formalism.L2.NX.MtVReal"
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

## Rational realizations of twisted theta expansions

[Definition / hypothesis ARAK.D219](https://andrewodesky.com/rh/lean/Formalism.L2.NExpTied/)

Use ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)), ([Automorphic realizations and normalized Hecke operators](https://andrewodesky.com/rh/lean/Formalism.L2.NGalTiedAlt/)), and ([Normalized Hecke characters and coefficient rings](https://andrewodesky.com/rh/lean/Formalism.L2.NC.NChiData/)). Write $r$ for the finite-type rank, $n=r+t$, $O_i$ for a twist coefficient ring, $K_i=\operatorname{Frac}(O_i)$ and $K_{i,k}=\operatorname{Frac}(O_{i,k})$.

Hypothesis (normalized theta realizations). The specified subgroup of the generator matrix product is exactly the product of upper unitriangular groups. Its character on every coefficient side is a product of nontrivial additive characters of the first-superdiagonal sums, with nontriviality required when $r\ge2$. The two sides have inverse characters. For each side there are also additive characters $\vartheta_a:\mathbb F_{g_a}\to K_i^\times$, nontrivial when $r\ge2$, such that $$\psi_{i,b}(u)=\prod_{(a,v)}\vartheta_a\left(\bar\xi_{0,a,v}\sum_{l=0}^{r-2}(u_{a,v})_{l,l+1}\right).$$ Here $\bar\xi_{0,a,v}$ is the reduction of $\xi_0$ at the prescribed generator prime.

For each admitted auxiliary set $Q$ and exponent $M$, the $P$-coordinate of the homomorphism $\delta_{i,Q,M}$ in ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)) is surjective on inertia at $P\in Q$ and zero on inertia at every $P'\in Q$ distinct from both $P$ and its conjugate. The universal theta vector for $Q=\varnothing$ is the ordinary theta vector tensored with the unit of the trivial group algebra, at every selected stage. The two sign choices used below are both equal to $1$.

For every $i,j,b$ choose a finite-dimensional $K_i$-space $W_{i,j,b}$ and a representation $\rho_{i,j,b}$ of $G_n(F)$. At selected stages it is irreducible and algebraic: for some rational basis of $E$ and coefficient basis of $W_{i,j,b}$, its matrices are polynomials over $K_i$ in the rational coordinates of the entries of rational unitary matrices. Choose a multiplicative residue character $\tau_{i,j,b,a,v}$ at every generator label. If that generator prime is not over $\ell_i$ and $u\in\mathcal O_E$ has residue $x\in\mathbb F_{g_a}^\times$, require $$\tau_{i,j,b,a,v}(x)=\text{the coefficient image of }\operatorname{tame}(\chi^{(1),\rm Gal}_{i,j,b},P,u).$$ The tame value of a Galois character at $(P,u)$ is its value at a chosen inertia element $\sigma$ for which, for some uniformizer $\varpi_P$ and root $y^{NP-1}=\varpi_P$, the residue of $\sigma(y)/y$ equals that of $u$; if no such element exists the value is one. The same convention with $u^e$ defines exponent $e$.

For every admissible twist $(i,k,Q,\chi)$ and selected stage, choose a finite-dimensional irreducible $K_{i,k}$-representation $\widetilde\rho$ on $\widetilde W$, algebraic in the same rational-coordinate polynomial sense, with bases identifying its matrices with those of $\rho_{i,j,b}$ after coefficient extension. Choose a subgroup $J\subseteq G_n(\mathbb A_{F,f})$ and character $\chi_J:J\to K_{i,k}^\times$, trivial on some positive principal congruence subgroup. The expansion-input space is linearly isomorphic over $K_{i,k}$ to the full automorphic $J$-character subspace with coefficient representation $\widetilde\rho$. Explicitly these are all functions $f$ satisfying $f(\gamma g)=\widetilde\rho(\gamma)f(g)$ and $f(gk)=\chi_J(k)f(g)$; the principal-congruence condition above ensures their smoothness.

Choose subsets $Q^+\subseteq Q$ and $D^+\subseteq P_{\Delta,i}$ containing exactly one prime from each conjugate pair in their respective sets: each prime has itself or its conjugate in the chosen subset, and no two chosen primes are conjugate. Choose a split local realization at every prime; its selected CM prime equals $P$ whenever $P\in Q^+\cup D^+$ or is a generator prime. At generator primes choose ring maps from the local integers of $F$ to $\mathbb F_{g_a}$.

The subgroup $J$ consists exactly of globally maximal-compact elements satisfying the following local conditions. At generator primes the lower-left $(n-r)\times r$ block vanishes modulo the maximal ideal and the leading $r\times r$ block is upper unitriangular modulo it. At $Q^+\cup D^+$ require only the lower-left vanishing. Outside the primes below $Q$, generator primes and delta primes, the local subgroup is maximal compact and the character is trivial.

Its character is the product of three factors. At a generator prime, reduce the leading $r\times r$ block and apply its contribution to the specified unitriangular character; multiply by $\tau_{i,j,b,a,v}$ on the reduced trailing-block determinant. At a prime in $Q^+$ apply the twisting Galois character's tame value to an integral residue representative of the trailing determinant, with exponent $1$. At a prime in $D^+$ use the delta Galois character, with exponent $1$ on the true side and $-1$ on the false side. Transport all values through their prescribed coefficient embeddings. In this formula a nonintegral local value has integral lift zero, a noninvertible reduced leading block is replaced by the identity, and a nonunit trailing determinant contributes one. Extend the unitriangular character by one outside its domain. These conventions specify the character formula on every matrix on which it is evaluated.

For every selected stage and embedding of $E$ through the indicated coefficient-side embedding into $K_i$, the dual of $\rho_{i,j,b}$ has a highest weight. Every such highest weight has the precise shifted infinitesimal multiset prescribed in ([Automorphic realizations and normalized Hecke operators](https://andrewodesky.com/rh/lean/Formalism.L2.NGalTiedAlt/)) by the fixed weights and the recorded singleton eta parameter. Highest weight over $K_i$ has the same polynomial-matrix and upper-triangular eigenvector meaning, with $B^{-\mathsf T}$ substituted at the conjugate embedding.

An admissible twist here has the auxiliary-prime conditions of ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)), avoids all generator and delta primes, has open kernel, is inverted by the fixed complex conjugation, has values of $\ell_i$-power order, and is unramified outside $Q$. All subgroup, representation and coefficient choices above retain their displayed selected-stage restrictions; the generic-character and universal-continuity conditions have their stated full stage ranges.
