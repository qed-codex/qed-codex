---
{
  "module": "src/Formalism/LocalToGlobal/NormalizedHeckeFactors/GlobalDatumRegularityOfTypesCompatibility.lean",
  "declarations": [
    "Formalism.L2.NormalizedTypesCompatibility"
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

## Polynomial labels and normalized finite types

[Definition / hypothesis REP.D220](https://andrewodesky.com/rh/lean/Formalism.L2.NormalizedTypesCompatibility/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), ([Local parameter systems for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NAut/)) and ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)). Write $E_0$ for the imaginary quadratic subfield and $\jmath_E:E\hookrightarrow\overline{\mathbb Q}$ for the chosen embedding. For $K=\jmath_E(E_0)$ and $M=Q_Sqd$, define $R(K,M)$ as the compositum of all finite extensions $L/\mathbb Q$ in $\overline{\mathbb Q}$ containing $K$ with this property: every rational prime $p$ admitting an integral $\pi\in K$, with $(\pi-1)/M$ integral and $\pi\alpha(\pi)=p$ for some $\mathbb Q$-embedding $\alpha:\overline{\mathbb Q}\to\overline{\mathbb Q}$, splits completely in $L$. This compositum is the literal construction used here.

Hypothesis (normalized finite types). The recorded field $M_{\rm rec}$ is isomorphic to $R(K,M)$ by an isomorphism extending $\jmath_E$ on $E_0$. At each generator prime $g_a$, choose a valuation subring $A_a\subseteq\mathbb C$ with residue field identified with $\overline{\mathbb F}_{g_a}$. Every value of the recorded multiplicative lift $\omega_a$ is integral in $A_a$ and reduces to its argument.

For every local coefficient record $i$, there is a valuation subring $B_i\subseteq\mathbb C$ with residue field identified with $\overline{\mathbb F}_{\ell_i}$. All values of the complex embedding of $O_i$ are integral in $B_i$, and their reductions agree with the recorded residual coefficient embedding. Every recorded finite-type map $\iota_{a,v,w(i)}$ is reduction of $\omega_a$ through this same $B_i$. Reduction of a nonintegral complex number is defined to be zero.

Choose generators $\zeta_{a,d}\in\overline{\mathbb F}_{g_a}$ for all $d>0$, of order $g_a^d-1$, satisfying $$\zeta_{a,d'}^{(g_a^{d'}-1)/(g_a^d-1)}=\zeta_{a,d}\qquad(d\mid d',\ d'>0).$$ For every finite-dimensional complex representation $\tau$ of $\mathrm{GL}_d(\mathbb F_{g_a})$, choose a polynomial $L_a(\tau)\in\mathbb F_{g_a}[X]$. Isomorphic representations have the same polynomial. If $d\ge1$ and $\tau$ is irreducible cuspidal, its polynomial is monic irreducible of degree $d$ and differs from $X$; equality of these polynomials for two such representations implies that they are isomorphic. Cuspidal here means that the fixed vectors of every proper block upper-unitriangular radical are zero.

In dimension one impose the following normalization. If $x\in\mathbb F_{g_a}^\times$ and the character of $\tau$ at $\gamma$ is $\omega_a(x)^m$ whenever $\zeta_{a,1}^m=\det\gamma$, then $L_a(\tau)=X-x$.

The polynomial labels obey two equivariance laws. If a complex automorphism $\alpha$ acts as $z\mapsto z^h$ on roots of unity of order dividing $\prod_{e=1}^d(g_a^e-1)$, and the character of $\tau'$ is obtained by applying $\alpha$ to that of $\tau$, then the roots of $L_a(\tau')$ are the $h$th powers of the roots of $L_a(\tau)$, with multiplicity. If the character of $\tau'$ at $\gamma$ is that of $\tau$ at $\gamma^{-1}$, its roots are the inverses of those of $L_a(\tau)$. Also, if for $x\in\mathbb F_{g_a}^\times$ the character of $\tau'$ at $\gamma$ is $\omega_a(x)^m$ times that of $\tau$ whenever $\zeta_{a,1}^m=\det\gamma$, then its roots are those of $L_a(\tau)$ multiplied by $x$. These assertions concern irreducible cuspidal $\tau,\tau'$ of positive dimension.

The recorded central idempotent $e_{a,f}$ is the sum of the central irreducible idempotents of all irreducible representations with polynomial label $f$. For a general irreducible representation its label is the product of the labels of an irreducible cuspidal block tuple in a parabolically induced representation containing it. More explicitly, choose a partition of the coordinate indices into nonempty ordered blocks, a cuspidal irreducible representation on each block, and induce their exterior tensor product from the block parabolic, with its unipotent radical acting trivially; require the given representation to be a constituent and the product to equal $f$. The idempotent of $\tau$ has coefficient $$\frac{\dim\tau}{|\mathrm{GL}_r(\mathbb F_{g_a})|}\operatorname{tr}(\tau(\gamma^{-1}))$$ at $\gamma$.

For each generator-place label choose a residue-field isomorphism for the fixed valuation of $\Omega$ above that prime. The recorded tame element $t_{a,v}$ is coupled to the chosen generators by $$\operatorname{red}\bigl(t_{a,v}(y)/y\bigr)=\zeta_{a,d}\quad\text{whenever }d>0,\quad y^{g_a^d-1}=g_a.$$

Finally the recorded parameter set is in bijection with lists of terms $(a,\pi,d)$ such that $a,d\ge1$, $\pi$ is a recorded conjugate-self-dual cuspidal class of rank $a$, no triple is repeated and $\sum ad=r$. At every generator place the finite inertia polynomial of the list's local parameter is monic of degree $r$. Under this bijection, the recorded parameter at every finite prime is exactly the isobaric local parameter of the list. An isobaric local parameter is the direct sum of the local parameters of $\pi$ with the norm shifts $(d-1)/2-c$ for $0\le c<d$, using the direct-sum, zero-parameter and norm-shift operations of ([Local parameter systems for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NAut/)); the equality concerns that full local parameter, not merely its polynomial label.
