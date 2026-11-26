---
{
  "module": "src/Formalism/LocalToGlobal/GaloisLevelStructure/TiedHecke.lean",
  "declarations": [
    "Formalism.L2.AVTied",
    "Formalism.L2.HeckeTied"
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

## Automorphic realizations and normalized Hecke operators

[Definition / hypothesis ARAK.D214](https://andrewodesky.com/rh/lean/Formalism.L2.NGalTiedAlt/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)), and ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). Write $E/F$ for the CM extension, $n=n_V=r+t$, $G_n(F)$ for its rational unitary group and $G_n(\mathbb A_{F,f})$ for its finite adelic group. A principal congruence subgroup of positive integer level $N$ consists of integral unitary matrices congruent to one modulo $N$.

An algebraic coefficient representation is a finite-dimensional complex representation $\rho$ of $G_n(F)$ whose matrices in some basis are polynomials in the entries of the rational unitary matrix under all complex embeddings of $E$. An automorphic function of coefficient representation $\rho$ is a function $f:G_n(\mathbb A_{F,f})\to W_\rho$ with $f(\gamma g)=\rho(\gamma)f(g)$, fixed on the right by some positive principal congruence subgroup. An irreducible automorphic subspace is a nonzero right-translation-stable subspace of these functions with no proper nonzero such subspace. Its isotypic space is the sum of all irreducible subspaces isomorphic to it; its multiplicity is the dimension of the space of equivariant maps from it to all automorphic functions of that coefficient representation.

Hypothesis (automorphic realizations). Choose an embedding $E\hookrightarrow\overline{\mathbb Q}$ and an isomorphism from the fixed algebraic closure $\Omega/E$ to $\overline{\mathbb Q}$ extending it. For every tuple $\mu$ and $1\le j\le m$, choose an irreducible algebraic coefficient representation $\rho_{\mu,j}$, a subgroup $J_{\mu,j}\subseteq G_n(\mathbb A_{F,f})$, a character $\chi_{\mu,j}:J_{\mu,j}\to\mathbb C^\times$ trivial on some positive principal congruence subgroup, and an injective linear map $$\mathcal R_{\mu,j}:M_{\mu,j}\longrightarrow\{\text{automorphic functions of coefficient representation }\rho_{\mu,j}\}.$$ Its image is exactly the subspace satisfying $f(gk)=\chi_{\mu,j}(k)f(g)$ for every $k\in J_{\mu,j}$.

For a local record $a$, call a prime $P$ good when it is split in the CM extension, is not above $\ell_a$, and is outside both recorded sets $S_a,Q_a$. At a split prime choose the indicated local matrix realization and a uniformizer $\varpi$. The normalized Hecke operator is $$T_{P,k}f(g)=q_P^{-k(n-1)}\sum_{\gamma\in J\backslash J\alpha_{P,k}J}f(g\gamma),\qquad 1\le k\le n,$$ where $\alpha_{P,k}$ has $k$ uniformizer entries and $n-k$ unit entries in that split realization. Equivalently the sum uses the source's finitely supported sum over right $J$-cosets meeting this double coset.

At every local record, away from $Q_a$, the generator primes and the selected opposite delta prime, the level is maximal compact with trivial character. Whenever rational vectors $x,x'$ satisfy $\mathcal R(jx')=T_{P,k}\mathcal R(jx)$ at a good prime, their local projections satisfy $$\operatorname{pr}_a(x')=h_{a,P,k}\operatorname{pr}_a(x).$$ Every normalized Hecke image of a rational vector is realized by some rational $x'$. These assertions hold for every compatible split realization and uniformizer.

Records with the same stage and coefficient prime have coefficient-ring isomorphisms preserving their complex embeddings. For every such isomorphism between distinct records and every pair of their eigenvalue labels, some prime good for both and some $1\le k\le n$ distinguish the two eigenvalues by a unit difference. Each $Q_a$ is closed under CM conjugation, and $Q_a=Q_{a'}$ whenever their coefficient primes agree.

For every recorded local automorphic label $P$ choose an irreducible automorphic subspace $\Pi_{a,P}$. Isomorphic choices have equal labels. Every irreducible automorphic subspace whose isotypic component has nonzero inverse image under $\mathcal R$ has such a label. Its isotypic inverse image is exactly the recorded type space. The optional recorded eigenvalue label is $x$ if and only if, on that whole type space, every good $T_{P,k}$ acts by the complex image of $h_{a,P,k}(x)$.

For each selected stage choose maps from actual irreducible automorphic representations and actual irreducible algebraic weights onto the recorded automorphic and weight classes. Each map identifies precisely isomorphism classes. The automorphic map preserves multiplicities. At nonsplit CM primes, the recorded spherical condition is equivalent to existence of a nonzero vector fixed by the corresponding single-prime maximal compact subgroup. Whenever a Satake tuple exists, one such tuple has exactly the recorded Satake multiset. A Satake tuple here means a nonzero local maximal-compact fixed vector on which every spherical Hecke function acts by its Satake-transform value at that tuple. The class of $\Pi_{a,P}$ is the recorded image of $P$.

If an algebraic weight $a$ is dual to the coefficient weight of an automorphic representation, its recorded weight class is that of $a$. Duality means a nonzero invariant bilinear pairing. If $\lambda=(\lambda_0,\ldots,\lambda_{n-1})$ is a highest weight at $\tau$, the recorded infinitesimal multiset is $$\{\lambda_i+(n-1)/2-i:0\le i<n\}.$$ Highest weight means that, in a polynomial matrix realization of the algebraic representation, a nonzero vector transforms under every upper triangular matrix $B$ by $\prod_iB_{ii}^{\lambda_i}$, substituting $B$ at $\tau$, $B^{-\mathsf T}$ at $\bar\tau$, and identity at the other embeddings.

Hypothesis (local levels). Choose the tuple Hecke characters $\xi_{\mu,j}$. For every local record $a$, put $\mu=\mu(a)$ and $j=j(a)$. The following product, ramified-place, generator-place and outside-place conditions hold for $J_{\mu,j},\chi_{\mu,j}$. Every element of $J_{\mu,j}$ has, at every finite prime $v$ of $F$, a single-prime-supported element of $J_{\mu,j}$ with the same local matrix. Let $Q(\xi)$ be the primes of $F$ outside the generator set lying below some CM prime where $\xi$ is ramified. Outside the generator set and $Q(\xi_{\mu,j})$, the level is maximal compact and its character is trivial.

At each $v\in Q(\xi_{\mu,j})$ choose a split realization and a local character $\xi_v$ agreeing with the tuple Hecke character on $E^\times$ and trivial on a sufficiently small principal unit group. The single-prime part of $J$ consists exactly of integral invertible matrices whose lower-left $(n-r)\times r$ block vanishes modulo the maximal ideal. Its character is $\xi_v$ of the determinant of the trailing $(n-r)\times(n-r)$ block. At each generator prime require also that the leading $r\times r$ block is upper unitriangular modulo the maximal ideal. Its character is the product of $\xi_v$ on the trailing determinant and $\psi_v$ on the sum of the first $r-1$ superdiagonal entries. Here $\psi_v$ is trivial on the maximal ideal and nontrivial on the ring of integers.

For every tuple $\mu$ and every selected stage $1\le j\le m$, if the recorded eta parameter at $\tau$ is $\{s\}$ and $\lambda$ is any highest weight of a dual coefficient representation, require $$\{\lambda_i+(n-1)/2-i\}_i=\{v_i-s:0\le i<k-1\}+\{-b_i-s:0\le i<m\}+\{-e_{j-1}-s+(t-1-2c)/2:0\le c<t\}.$$ The weights $v_i,b_i,e_i$ are those of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)).
