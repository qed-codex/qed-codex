---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/GeometricRealizationOfWeightOne.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one",
    "UpperTheory.Gal.Int.Geo.steps_holds"
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

## Seventeen statements on Galois representations carried by the cohomology of a scheme with correspondences

[Theorem AGR.0021](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.steps_holds/)

The theorem has no hypotheses. It is the conjunction of the seventeen statements below. The statements use the terms defined in *([Schemes with correspondences and the Galois representations they carry](https://andrewodesky.com/rh/lean/GlobalTheory.GalV.HTower/))* and in *([Local conditions on an l-adic representation of the Galois group of a number field](https://andrewodesky.com/rh/lean/GlobalTheory.RoadWGeo.ESAt/))*: a scheme with correspondences $H=(Z,\Gamma,(Y_g,s_g,t_g))$, smooth projective; a representation carried by $(H,\theta)$; models at a place, good reduction, the congruence relation; the Hecke polynomial $P_{w,n,\vartheta}$ and its multiset of roots; occurrence of $\theta$ in a Hodge degree; and, for a representation of $G_E$, inverse Frobenius killed by a polynomial, crystalline at $w$, Hodge–Tate multisets, crystalline with Frobenius eigenvalues in $R$, and the class $(c,m)$ of a character.

Each statement holds for every number field $E$ with algebraic closure $\bar E$ and $G_E=\operatorname{Aut}(\bar E/E)$, every prime $\ell$, every ring isomorphism $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$, every finite place $w$ of $E$, and all the other data it names. Representations are homomorphisms $G_E\to GL_d(\overline{\mathbb Q}_\ell)$, continuous only where this is said; a representation is *semisimple* if every invariant subspace of $\overline{\mathbb Q}_\ell^{\,d}$ has an invariant complement.

**A. Cohomology.** Let $H$ be a smooth projective scheme with correspondences over $E$ and $\theta\colon\Gamma\to\overline{\mathbb Q}_\ell$. In statements 2 to 5, $\rho$ is a continuous representation carried by $(H,\theta)$, $n\ge0$, $\vartheta$ is a sequence in $\overline{\mathbb Q}_\ell$, and $R$ is a finite multiset of complex numbers.

1. There are $d\ge0$ and a continuous semisimple representation $G_E\to GL_d(\overline{\mathbb Q}_\ell)$ carried by $(H,\theta)$.
2. Suppose $w\nmid\ell$, $(H,\theta)$ satisfies the congruence relation of degree $n$ with coefficients $\vartheta$ at $w$, and $R$ is the multiset of roots of $P_{w,n,\vartheta}$. Then $\rho$ is unramified at $w$ and $\prod_{r\in R}(X-r)$ kills its inverse Frobenius.
3. Suppose $w\mid\ell$ and $(H,\theta)$ has a surjective model at $w$. Then $\rho$ is crystalline at $w$.
4. Suppose $w\mid\ell$ and $(H,\theta)$ has good reduction at $w$. Then the Hodge–Tate multisets of $\rho$ at $w$ contain the set of pairs $(\tau,j)$ such that $\theta$ occurs in Hodge degree $j$ at $\tau$.
5. Suppose $w\mid\ell$, $(H,\theta)$ satisfies the congruence relation of degree $n$ with coefficients $\vartheta$ at $w$, and $R$ is the multiset of roots of $P_{w,n,\vartheta}$. Then $\rho$ is crystalline at $w$ with Frobenius eigenvalues in $R$.
6. Here $\theta$ may take values in any field $L$. If $(H,\theta)$ has weak good reduction at $w$, it has good reduction at $w$. If it satisfies weakly the congruence relation of degree $n$ with coefficients $\vartheta$ at $w$, it satisfies that congruence relation at $w$.

**B. Twisting by a character.** Let $\rho\colon G_E\to GL_d(\overline{\mathbb Q}_\ell)$ and $\chi\colon G_E\to\overline{\mathbb Q}_\ell^\times$ be continuous, $c\in\mathbb C$, $m$ a function from the embeddings $E\to\mathbb C$ to $\mathbb Z$, and suppose $\chi$ has class $(c,m)$ at $w$. Write $cR$ for the multiset $\{cr:r\in R\}$.

7. If $w\nmid\ell$, $\rho$ is unramified at $w$ and $\prod_{r\in R}(X-r)$ kills its inverse Frobenius, then $\chi\rho$ is unramified at $w$ and $\prod_{r\in cR}(X-r)$ kills its inverse Frobenius.
8. If $\rho$ is crystalline at $w$, so is $\chi\rho$.
9. Let $Q$ be a set of pairs $(\tau,j)$ with $\tau\colon E\to\mathbb C$ and $j\in\mathbb Z$. If the Hodge–Tate multisets of $\rho$ at $w$ contain $Q$, then those of $\chi\rho$ at $w$ contain $\{(\tau,j+m(\tau)):(\tau,j)\in Q\}$.
10. If $\rho$ is crystalline at $w$ with Frobenius eigenvalues in $R$, then $\chi\rho$ is crystalline at $w$ with Frobenius eigenvalues in $cR$.

**C. Satake parameters and weights.** Let $q=N(w)$, $a\ge0$, and $\rho\colon G_E\to GL_d(\overline{\mathbb Q}_\ell)$ any representation.

11. Let $B$ be a multiset of $a$ nonzero complex numbers. Suppose $\rho$ is crystalline at $w$ with Frobenius eigenvalues in the multiset $\{q^{(a-1)/2}\beta:\beta\in B\}$. Then for every place $A$ of $\bar E$ above $w$ and all local data at $A$, $\rho|_{D_A}$ is crystalline, and there are $g\in W_A$ of degree $-1$ and $m\ge0$ such that the characteristic polynomial of $g$ on $\mathrm{WD}(\rho|_{D_A})$ divides the $m$-th power of the characteristic polynomial of $g$ on $\bigoplus_{\beta\in B}\psi_\beta$, where $\psi_\beta$ is the character $\sigma\mapsto(\beta^{-1}q^{(1-a)/2})^{\deg\sigma}$ of $W_A$.

For statements 12 to 14, let $E$ be a CM field and $\mathcal A$ a complex vector space of functions on its adelic definite unitary group in $a$ variables. Use the definitions of local occurrence, Satake multisets, weights, $J(\lambda)$, lacunarity, embeddings over $w$, and Hodge–Tate multisets containing the weights of $\mathcal A$ from ([Satake multisets and weights of definite unitary forms](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)).

12. If $B$ is a Satake multiset of $\mathcal A$ at $w$, then $|B|=a$.
13. Let $Q$ be a set of pairs $(\tau,j)$ containing $(\tau,j)$ for every $\tau$ over $w$, every weight $\lambda$ of $\mathcal A$ at $\tau$ and every $j\in J(\lambda)$. If the Hodge–Tate multisets of $\rho$ at $w$ contain $Q$, they contain the weights of $\mathcal A$.
14. Suppose $w\mid\ell$, the Hodge–Tate multisets of $\rho$ at $w$ contain the weights of $\mathcal A$, and for some $\tau$ over $w$ some weight $\lambda$ of $\mathcal A$ at $\tau$ has $J(\lambda)$ lacunary. Then there exist a place $w'\mid\ell$ of $E$, a place $A$ of $\bar E$ above $w'$, local data at $A$, an embedding $\tau'\colon E\to\overline{\mathbb Q}_\ell$, a Hodge–Tate multiset $J$ of $\rho|_{D_A}$ at $\tau'$, and a lacunary set of $a$ integers contained in $J$.

**D. Characters attached to Hecke characters.** A *Hecke character* of $E$ is a continuous homomorphism from the idele group of $E$ to $\mathbb C^\times$ trivial on $E^\times$. For such $\chi$ and $n$ a function from the embeddings $E\to\mathbb C$ to $\mathbb Z$, call $\chi$ *algebraic of type $n$* if $\chi(k_\infty)=\prod_{\varphi\colon E\to\mathbb C}\varphi(k)^{n(\varphi)}$ for every $k\in E^\times$ that is positive at every real embedding, where $k_\infty$ is the idele equal to $k$ at the infinite places and to $1$ at the finite places. $\chi$ is *unramified at $w$* if its component $\chi_w$ is trivial on the units of $E_w$; then $\chi(\varpi_w)$ denotes the value of $\chi_w$ at an element of $E^\times$ of valuation $1$ at $w$.

15. There is a map $\Lambda$ from pairs $(\chi,n)$ to characters $G_E\to\overline{\mathbb Q}_\ell^\times$ such that: whenever $\chi$ is algebraic of type $n$, $\Lambda(\chi,n)$ is continuous and has class $(\chi(\varpi_w),-n)$ at every finite place $w$ where $\chi$ is unramified; and if $\chi$ is algebraic of type $n$, $\chi'$ algebraic of type $n'$, and $\Lambda(\chi,n)=\Lambda(\chi',n')$, then $\chi=\chi'$.

**E. Representations of an abstract group.** Let $\Gamma$ be a group, $k$ a field, $r\colon\Gamma\to GL_a(k)$, $s\colon\Gamma\to GL_b(k)$ representations and $c\colon\Gamma\to k^\times$ a character.

16. If $r\oplus s$ is semisimple, so is $r$. A conjugate $g\,r\,g^{-1}$ ($g\in GL_a(k)$) of a semisimple $r$ is semisimple. If $r$ is semisimple, so is $c\,r$.
17. Let $\Gamma$ be a topological group and $k$ a field with a topology making it a topological ring. If $r\oplus s$ is continuous, so is $r$. A conjugate of a continuous $r$ is continuous. If $r$ and $c$ are continuous, so is $c\,r$. If $c$ is continuous, so is $c$ viewed as a representation $\Gamma\to GL_1(k)$.

## Galois representations with local conditions, given a fixed-point trace formula

[Theorem AGR.1.1752](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one/)

Assume ([A fixed-point trace formula for finite étale correspondences](https://andrewodesky.com/rh/lean/UpperTheory.Gal.LocalSmoothExtension.HolomorphicLefschetzFormula/)). Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\bar E$ be an algebraic closure of $E$ and $G_E=\operatorname{Aut}(\bar E/E)$, let $\ell$ be a prime, let $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $a$ be an odd positive integer. Let $d$ be a positive integer such that $-d$ is a square in $E$ and in $\mathbb Q_\ell$, let $x\in E$ satisfy $x^2=-d$, and put $K=\mathbb Q(x)$. Assume that $[E^+:\mathbb Q]$ is even and that every finite place of $E$ that is nonsplit over $E^+$ is unramified over $E^+$ and does not divide $\ell$.

Let $U$ be an automorphic representation of the definite unitary group $\mathcal U$ in $a$ variables over $E$, and let $w_0$ and $v'$ be places of $E$ above $\ell$ that lie above different places of $E^+$ and above the same place of $K$. Assume the following four conditions.

- (a) $U$ is unramified at all but finitely many of the nonsplit places of $E$.
- (b) $U$ has a Satake multiset at all but finitely many of the split places of $E$.
- (c) There are an integer $m\ge1$, a compact open subgroup $\Gamma$ of $GL_a(E_{w_0})$ whose only element of finite order is the identity, a surjective homomorphism $\theta\colon\Gamma\to\mathbb Z/\ell^m\mathbb Z$ and a nontrivial character $\chi\colon\mathbb Z/\ell^m\mathbb Z\to\mathbb C^\times$ with the following two properties. Every smooth irreducible complex representation $(\pi,V)$ of $GL_a(E_{w_0})$ that has a nonzero vector $\xi$ with $\pi(\gamma)\xi=\chi(\theta(\gamma))\xi$ for all $\gamma\in\Gamma$ is cuspidal. Some nonzero $f\in U$ satisfies $R_gf=\chi(\theta(g_{w_0}))f$ for every $g\in\mathcal U_{w_0}$ with $g_{w_0}\in\Gamma$.
- (d) $U$ has a Satake multiset at $v'$ and a lacunary weight at $v'$.

Then the following three assertions hold.

1. There are an integer $n\ge0$ and a representation $\rho\colon G_E\to GL_n(\overline{\mathbb Q}_\ell)$ that satisfies the base conditions.
2. Let $w$ be an eligible place of $E$ that does not divide $\ell$ and at which $U$ has a Satake multiset. There are an integer $n\ge0$ and a representation $\rho\colon G_E\to GL_n(\overline{\mathbb Q}_\ell)$ that satisfies the base conditions such that, for every Satake multiset $B$ of $U$ at $w$, $\rho$ is unramified at $w$ and $\prod_{r\in R_w(B)}(X-r)$ kills its inverse Frobenius.
3. Let $w$ be a place of $E$ above $\ell$ that lies above the same place of $K$ as $v'$, lies above a place of $E^+$ different from those below $w_0$ and $v'$, and at which $U$ has a Satake multiset. There are an integer $n\ge0$ and a representation $\rho\colon G_E\to GL_n(\overline{\mathbb Q}_\ell)$ that satisfies the base conditions such that $\rho$ is crystalline at $w$ and the Hodge–Tate multisets of $\rho$ at $w$ contain the weights of $U$. There are also an integer $n'\ge0$ and a representation $\rho'\colon G_E\to GL_{n'}(\overline{\mathbb Q}_\ell)$ that satisfies the base conditions such that, for every Satake multiset $B$ of $U$ at $w$, $\rho'$ is crystalline at $w$ with Frobenius eigenvalues in $R_w(B)$.
