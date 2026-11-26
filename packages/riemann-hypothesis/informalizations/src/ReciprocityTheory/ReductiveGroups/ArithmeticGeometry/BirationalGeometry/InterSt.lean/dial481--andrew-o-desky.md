---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterSt.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.PtsIntegrableStatement"
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

## Three further assumptions for the tower volume bound: integrability, the Weil pairing and comparison under automorphisms

[Definition / hypothesis ARAK.D266](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.PtsIntegrableStatement/)

The following three statements are assumed, together with others, in the uniform volume and slope bounds for root towers.

**(1) Integrability of logarithmic norms.** Use the notation of ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)). Let $P$ be an arithmetic variety of dimension $e+1$ in a finite coordinate system, and let $\Phi:\mathbb C^{\prod_bI_b}\to\mathbb C^{e+1}$ be a complex-linear map that is nonzero at $\operatorname{Seg}(z)$ for every $z\in\mathcal C_P$. Let $L_1,\dots,L_e$ and $A$ be smooth Hermitian line data, and let $s\notin P$ be an integral polynomial that is multihomogeneous of multidegree equal to that of $A$. For $y\in\mathbb C^e$ let $F(y)$ be the sum, over all $w=\operatorname{Seg}(z)$ with $z\in\mathcal C_P$ and $\Phi w=(1,y)$, of the contributions that define the logarithmic intersection integral $\mathcal I_P(L_1,\dots,L_e;\log\|s\|_A)$ when the map $\Phi$ is used. Then $F$ is Lebesgue integrable on $\mathbb C^e$.

**(2) The Weil pairing from theta groups.** Let $S$ be a locally Noetherian scheme, $(A,L)$ a polarized abelian scheme over $S$ with its line bundle, $k\ge0$ an integer and $T$ an $S$-scheme. For $x,y\in A(T)$ and a unit $c\in\Gamma(T,\mathcal O_T)^\times$, say that *$c$ is the level-$k$ commutator of $(x,y)$* if every point of $T$ has an open neighbourhood $V$ over which $x$ and $y$ lift to the level-$k$ theta group of $(A,L)$, and for every pair of such lifts over $V$ the commutator of the two lifts is the restriction of $c$ to $V$. The assumption is that the following four statements hold for all $S$, $(A,L)$, $k$ and $T$.

- If $kx=ky=0$, there is exactly one unit $c$ that is the level-$k$ commutator of $(x,y)$.
- If $c$ is the level-$k$ commutator of $(x,y)$ and $c'$ that of $(x',y)$, then $cc'$ is the level-$k$ commutator of $(x+x',y)$.
- If $kx=0$, then $1$ is the level-$k$ commutator of $(x,x)$.
- Let $l\ge0$ be an integer such that $kl$ is invertible on $T$, and suppose $klx=0$ and $ky=0$. Then $c$ is the level-$kl$ commutator of $(x,y)$ if and only if $c$ is the level-$k$ commutator of $(lx,y)$.

**(3) Comparison under automorphisms.** Let $I$ be a full intersection system. Take a CM host with field $E$, a polarized lattice datum of signature $(p,q)$, a level, a moduli scheme $X$ and a coefficient field $K$ as in ([Global models of unitary moduli schemes and geometric origins of root towers](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.IsGlobal/)), and put $\Psi$, $N=p+q$ and $d$ as there and in ([Root towers, their volumes and their slopes](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.RootModel/)). Let $O$ be a commutative ring with a ring homomorphism $\beta:O\to K$ for which $\operatorname{Spec}K\to\operatorname{Spec}O$ is a monomorphism, and let $Y$ be a model of $X$ over $\beta$. Suppose given

- an automorphism $g$ of the host, with underlying field automorphism $\sigma_g$ of $E$, an automorphism $\Phi$ of $X$ over its base, and a homomorphism over $\Phi$ from the twist by $g$ of the universal semiabelian object to the universal semiabelian object;
- a permutation $\pi$ of $\Psi$ with $\pi(\tau)=\tau\circ\sigma_g$ for every $\tau\in\Psi$;
- a finite set $S$ of natural numbers, a natural number $n$, two root models $M$ and $M'$ for $(\Psi,N)$, and Hodge ties of $M$ and of $M'$ to $Y$ relative to $(S,n)$, such that the compactification of the second tie is the image under $\Phi$ of that of the first and the two compactifications have the same exponent at every element of $S$.

Then, for every list $(\tau_0,i_0),\dots,(\tau_d,i_d)$ of $d+1$ pairs, $$\frac{I_{P_M}\bigl(L_{\tau_0,i_0}(t),\dots,L_{\tau_d,i_d}(t)\bigr)}{\delta_M}-\frac{I_{P_{M'}}\bigl(L'_{\pi(\tau_0),i_0}(t),\dots,L'_{\pi(\tau_d),i_d}(t)\bigr)}{\delta_{M'}}\ \longrightarrow\ 0\qquad(t\to0^+),$$ where $P_M$, $L_{\tau,i}(t)$, $\delta_M$ are the coordinate ideal, the lines and the integer $\delta$ of $M$, and $P_{M'}$, $L'_{\tau,i}(t)$, $\delta_{M'}$ those of $M'$.
