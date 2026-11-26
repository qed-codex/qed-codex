---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/UnitaryWeightExponentVectorSignatureWeightMuZero.lean",
  "declarations": [
    "GlobalTheory.FlagMod.FlagModel"
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

## Flag models and logarithmic Kodaira–Spencer maps

[Definition / hypothesis AG.D141](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)

Let $K$ be a commutative ring, let $X$ be a $K$-scheme, and let $\pi:G\to X$ be a semiabelian scheme with an $\mathcal O_E$-action for a CM number field $E$. Write $\bar a$ for CM conjugation. Fix a line bundle $\mathscr P$ on $G$ and an open subset $V\subseteq X$. Present $\mathscr P$ on an open cover with transition units $g_{ij}$, using the convention that local section coefficients satisfy $s_i=g_{ij}s_j$.

**Logarithmic derivations and tangent frames.** For an affine open $U\subseteq X$, put $A=\Gamma(U,\mathcal O_X)$ and let $I_U\subseteq A$ be the ideal of the reduced closed subset $(X\setminus V)\cap U$. Let $$\mathscr D_U=\{D\in\operatorname{Der}_K(A,A):D(I_U)\subseteq I_U\}.$$ An invariant tangent vector over $U$ is an $A[\epsilon]/(\epsilon^2)$-point of $G$, over $U$, whose reduction is the identity section. For every finite $A$-basis $v_1,\ldots,v_n$ of these vectors, define the action matrices $C(a)$ by $$[a]_*v_i=\sum_jC(a)_{ij}v_j.$$ Their balanced symmetric matrices form the $A$-module $$\mathscr B_C=\{\Theta\in M_n(A):\Theta^{\mathsf T}=\Theta,\ C(a)^{\mathsf T}\Theta=\Theta C(\bar a)\ \text{for all }a\in\mathcal O_E\}.$$

For any $A$-algebra $S$ and point $g\in G(S)$ over $U$, translate the scalar extension of $v_a$ by $g$. If $f$ is regular on an open containing the image of $g$, write $(v_af)(g)$ for the coefficient of $\epsilon$ in its value at this translated dual-number point.

**The local Kodaira–Spencer identity.** For $D\in\mathscr D_U$ and any matrix $\Theta\in M_n(A)$, require the following condition. There is an open cover $(W_i)$ of $\pi^{-1}(U\cap V)$ refining the chosen trivializations of $\mathscr P$, and there are absolute derivations over $\mathbb Z$, denoted $d_i$, of regular functions on $W_i$ and all its smaller opens, commuting with restriction. They lift $D$: for every $r\in A$, $$d_i(\pi^*r)=\pi^*(Dr)\quad\text{on }W_i.$$ On every open $O\subseteq W_i\cap W_j$, for every regular function $f$ on $O$, every commutative $A$-algebra $S$ with structure map $\varphi:A\to S$, and every $S$-point $g$ over the point of $U$ specified by $\varphi$, with image in $O$, require $$((d_i-d_j)f)(g)=\sum_{a,b=1}^n\varphi(\Theta_{ab})\, (v_bg_{ij})(g)\,g_{ij}(g)^{-1}\,(v_af)(g).$$ Here $g_{ij}$ is the transition unit of the two selected line-bundle trivializations, restricted to the overlap. Its value at $g$ is a unit of $S$.

The *logarithmic Kodaira–Spencer condition* requires, for every affine $U$ and every finite tangent basis as above, an $A$-linear isomorphism $$\kappa_U:\mathscr D_U\xrightarrow{\sim}\mathscr B_C$$ such that, for every $D\in\mathscr D_U$ and every $\Theta\in M_n(A)$, the local Kodaira–Spencer identity holds if and only if $\Theta=\kappa_U(D)$. The open cover and local lifts in that identity may depend on $D$ and $\Theta$. The basis length $n=0$ is allowed.

**Compactified flag models.** For this construction, take $K$ to be the coefficient number field.

Assume ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)), ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)), and ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)). Let $B/K$ be a normal, flat, projective model with a dense open immersion $X\hookrightarrow B$. The universal semiabelian family extends over $B$, retaining its action, rigidification, cubical polarization and bilinear-bundle relations; its abelian locus is exactly $X$. Require $B$ to be smooth of dimension $\lfloor[E:\mathbb Q]/2\rfloor p_{\rm sig}q_{\rm sig}$ and $B\setminus X$ to be a simple normal crossings divisor.

A flag model here is a proper morphism $\mathcal F\to B$, with $\mathcal F$ normal and flat over $K$. It carries an open atlas of tangent frames: the frame matrices have left inverses and, after changing base tangent charts, differ by upper triangular matrices on overlaps. The base charts are affine with integral-domain coordinate rings, carry tangent bases and the matrices of the $\mathcal O_E$-action compatibly with arbitrary base change, and carry polarization sections generating all sections over every smaller base open and nonzero on each fiber. For every embedding $\tau$, let $\mathscr F_{\tau,i}$ be the span of its first $i$ frame vectors. The successive quotients $\mathscr L_{\tau,i}=\mathscr F_{\tau,i+1}/\mathscr F_{\tau,i}$ define the graded line bundles. The open flag locus is dense. On the open moduli locus, for every embedding $\tau$, the span of the full $\tau$-flag is exactly the $\tau$-eigenspace of the tangent space. Every framed moduli point over every coefficient algebra lifts uniquely to $\mathcal F$ with those filtration steps, compatibly with every base change. Over every algebraically closed field, only finitely many flag points above a fixed base point have the same filtration steps.
