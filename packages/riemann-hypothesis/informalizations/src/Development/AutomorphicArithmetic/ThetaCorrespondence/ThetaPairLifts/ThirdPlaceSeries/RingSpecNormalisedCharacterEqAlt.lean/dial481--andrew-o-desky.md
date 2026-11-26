---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RingSpecNormalisedCharacterEqAlt.lean",
  "declarations": [
    "Formalism.L2.NTiedAllAlt"
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

## Compatibility of normalized Galois and theta data

[Definition / hypothesis ARAK.D228](https://andrewodesky.com/rh/lean/Formalism.L2.NTiedAllAlt/)

Hypothesis (normalized Galois and theta compatibility). For the same arithmetic family member impose ([Automorphic realizations and normalized Hecke operators](https://andrewodesky.com/rh/lean/Formalism.L2.NGalTiedAlt/)), ([Local Hecke algebras and normalized blocks](https://andrewodesky.com/rh/lean/Formalism.L2.NormalizedDataCompatibility/)), ([Normalized Hecke characters and coefficient rings](https://andrewodesky.com/rh/lean/Formalism.L2.NC.NChiData/)), ([Local coefficient rings and normalized twists](https://andrewodesky.com/rh/lean/Formalism.L2.TwFrame/)), ([Rational realizations of twisted theta expansions](https://andrewodesky.com/rh/lean/Formalism.L2.NExpTied/)), ([Polynomial labels and normalized finite types](https://andrewodesky.com/rh/lean/Formalism.L2.NormalizedTypesCompatibility/)), ([Compatible choices of normalized twists](https://andrewodesky.com/rh/lean/Formalism.L2.NChoiceTied/)), ([Integral and theta compatibility for families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Extra/)), and ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). The choices in these hypotheses are shared in the identities below. Write $K$ for the coefficient field and $K_0$ for its designated fixed subfield. At a coefficient prime $w$, let $\mu_w^{\rm tw}$ be the delta-times-twist tuple whose Hecke character is $\delta_{\ell_w}\psi_w$ in ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)).

The recorded local valuation on every finite extension of $\mathbb Q_\ell$ agrees with the norm by $v(x)=q\Longleftrightarrow|x|=\ell^{-q}$ for every rational $q$. Each chosen bridge embedding of the global algebraic closure into a local algebraic closure identifies the chosen global valuation ring with the local unit ball. Require this for both the local coefficient bridges and the twist bridges.

At every twisted coefficient prime $w$, every selected stage, and every admissible chosen twist, there is an embedding $\iota_w:\operatorname{Frac}(O_w')\hookrightarrow\mathbb C$ satisfying $\iota_w\circ e_w=\jmath$ on $K$. The automorphic subgroup for $\mu_w^{\rm tw}$ is exactly the subgroup of its rational twisted theta-expansion realization. Their characters agree after the coefficient map $K_{i_w,k_w}\to\operatorname{Frac}(O_w')$ followed by $\iota_w$.

The tuple character of the automorphic realization is exactly the tuple character of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). The normalized $\eta$, every selected-stage $\mu_{0,j}$, every $\delta_i$ and every local $\psi_a$ agree as idele characters with, respectively, the character-frame $\eta$, its $\mu_{0,j}$, its delta selected by $\ell_i$, and the tuple-character twist at $w(a)$.

For every coefficient prime $w$ choose a valuation subring $B_w\subseteq\mathbb C$ and an isomorphism $k(B_w)\simeq\overline{\mathbb F}_{\ell_w}$. Every complex image of an element of a local coefficient ring $O_a$ with $w(a)=w$ lies in $B_w$, and its reduction agrees with the recorded residual coefficient map, after the fixed residue-characteristic identification. Every finite-type embedding at $w$ equals reduction of its complex multiplicative lift through this same $B_w$; reduction of nonintegral elements is zero.

At every prime $P$ at which the normalized $\eta$ is unramified with uniformizer value $\alpha$, the recorded local Galois parameter of $\eta$ has Frobenius eigenvalue multiset $\{\alpha^{-1}\}$. For every local record $a$, outside a finite set of primes, the same assertion holds for the recorded character parameter $\mu_{C,a}$ and the normalized Hecke character $\mu_{0,j(a)}\delta_{i(a)}\psi_a$. The complex embedding of the twist coefficient field composed with the chosen true-side embedding of $K_0$ is $\jmath|_{K_0}$. The false-side embedding of $x\in K_0$ is the true-side embedding of $\bar x$ whenever $\bar x\in K_0$.

Let $\mathscr F$ be the row-type label set, with its polynomials $F_{a,\sigma,v}$ and residue scalars $\chi_{a,v,j}$. Define $\mathcal G\subseteq\mathscr F$ by requiring, for each $a=0,1$, that $(F_{a,\sigma,v})_v$ satisfy the selected-polynomial conditions of ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)) both for $(\chi_{a,v,j})$ and their inverses. Thus this is precisely the squarefree-root, prime-to-$\ell$ separation, forbidden-root and factor-degree condition stated there.

Impose also the following residual and characteristic-zero Galois comparisons. A semisimple representation means that every invariant subspace has an invariant direct complement. The recorded residual representation $\bar\rho_{\sigma,w}$ is semisimple whenever some local record lies over $w$. If $\sigma\in\mathcal G$ and the row isotypic space for $(a,\sigma)$ is nonzero, let $\Sigma$ be any row parameter list: its terms $(d,\pi,e)$ have $d,e>0$, $\sum de=r$, and its isobaric parameter equals the recorded row parameter at every split place. For every continuous representation $R:G_E\to\mathrm{GL}_r(O_a)$ semisimple over the fraction field and satisfying, at almost every prime, $$\operatorname{charpol}(R(\operatorname{Frob}_P))=\operatorname{GalPol}\bigl(\operatorname{IsoLoc}(\Sigma,P)((1-r)/2)\bigr)$$ through the recorded complex coefficient embedding, require $$\operatorname{charpol}(\bar\rho_{\sigma,w(a)}(g))=\operatorname{charpol}(\overline{R}(g))\qquad(g\in G_E),$$ with the fixed residue-field identification on the two sides. Here $\operatorname{GalPol}(A)$ is the recorded polynomial $\det(X-\operatorname{Frob}_A)$ of the local parameter, and $A(s)$ is its norm shift.

The last Galois condition is an implication with the following four premises. Every nonzero row isotypic space admits a row parameter list, and for $\sigma\in\mathcal G$ all terms of its chosen list are conjugate self-dual and regular algebraic. Every conjugate-self-dual regular-algebraic recorded cuspidal class of positive rank $d$ admits a continuous semisimple $\overline{\mathbb Q}_{\ell_a}$-representation whose almost-everywhere Frobenius polynomial is its local parameter shifted by $(1-d)/2$. Every recorded rank-one class $\chi$ and real $s$ whose shifted infinite parameters are integers admit a continuous Galois character with local parameter $\chi(s)$ at all finite primes away from $\ell_a$, and de Rham parameter $\chi(s)$ above $\ell_a$, with jumps equal to the negatives of those shifted infinite parameters at each induced embedding. Finally, the infinite parameters of the recorded $\eta^{-1}$ become integers after the shift $-t/2$.

Whenever these four premises hold, every spectral label with stage and side compatible with a local record $a$ admits a row type $\sigma\in\mathcal G$ with nonzero row isotypic space. Fix the specified choice of a row list for each such type. If that list is the single full-rank term $(r,\pi,1)$, the spectral Galois representation, extended through the recorded coefficient map to $\overline{\mathbb Q}_{\ell_a}$, is conjugate to $$R_\pi\otimes\chi_{\eta^{-1},-t/2}.$$ The two representations on the right are the fixed choices supplied by the second and third premises, respectively. The implication concerns those fixed choices and their product.
