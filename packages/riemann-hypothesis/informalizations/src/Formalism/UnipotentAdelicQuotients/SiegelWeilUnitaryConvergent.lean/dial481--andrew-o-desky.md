---
{
  "module": "src/Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean",
  "declarations": [
    "HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent"
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

## Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n

[Definition / hypothesis THETA.D086](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)

**Setting.** Let $F$ be a totally real number field and $E$ a totally complex quadratic extension of $F$, with $\sigma$ the automorphism of $E$ over $F$ that every complex embedding of $E$ carries to complex conjugation. Let $M\ge 0$ and let $J$ be an $M\times M$ matrix over $E$ with $\sigma(J_{ji})=J_{ij}$ and $\det J\neq 0$. For a commutative $F$-algebra $R$ put $E_R=R\otimes_F E$, on which $\sigma$ acts through the second factor, and $$h(x,y)=\sum_{i,j}\sigma(x_i)\,J_{ij}\,y_j\qquad(x,y\in E_R^M),\qquad H(R)=\{g\in \mathrm{GL}_M(E_R):\ \sigma(g)^{\mathsf T}Jg=J\}.$$ Write $\mathbb A=\mathbb A_F$ for the adele ring of $F$, $F_\infty$ for its archimedean part, $\mathbb A_f$ for the finite adeles and $F_v$ for the completion at a finite place $v$. The group $H(F)$ is regarded as a subgroup of $H(\mathbb A)$.

For $n\ge 0$, an $n$-tuple $X=(X_1,\dots,X_n)$ of vectors in $E_R^M$ has Gram matrix $G(X)=(h(X_a,X_b))_{a,b}$, and $g\in H(R)$ acts by $gX=(gX_1,\dots,gX_n)$. Let $\mathrm{Herm}_n(R)$ be the group of $n\times n$ matrices $S$ over $E_R$ with $\sigma(S_{ba})=S_{ab}$.

**Self-dual measures.** Let $V$ be a locally compact abelian group and $\chi:V\times V\to\mathbb C$. A measure $\mu$ on $V$ is *self-dual for $\chi$* if it is a Haar measure and, for every continuous compactly supported $\Phi:V\to\mathbb C$ whose transform $\widehat\Phi(y)=\int\Phi(x)\chi(x,y)\,d\mu(x)$ is integrable, $\int\widehat\Phi(y)\chi(y,z)\,d\mu(y)=\Phi(-z)$ for all $z$.

Fix a character $\psi$ of $\mathbb A$: a continuous homomorphism $\mathbb A\to\mathbb C^\times$ of absolute value $1$, trivial on $F$ and not identically $1$. Let $\psi_\infty$ and $\psi_v$ be its restrictions to $F_\infty$ and to $F_v$. For $R=F_\infty$ or $R=F_v$, with $\psi_R$ the corresponding restriction, we use the self-dual measures

- on the space $(E_R^M)^n$ of $n$-tuples, for $\chi(X,Y)=\psi_R\big(\sum_a \mathrm{Tr}_{E_R/R}\,h(X_a,Y_a)\big)$;
- on $\mathrm{Herm}_n(R)$, for $\chi(S,T)=\psi_R\big(\tfrac12\mathrm{Tr}_{E_R/R}\,\mathrm{tr}(ST)\big)$.

**Local density.** Let $R$ be $F_\infty$ or $F_v$, let $\mu$ and $\nu$ be measures on $(E_R^M)^n$ and on $\mathrm{Herm}_n(R)$, and let $\Phi$ be a function on $(E_R^M)^n$. A function $g$ on $\mathrm{Herm}_n(R)$ is a *density of $\Phi$ along the Gram map* if $g$ is continuous on the set of $S$ with $\det S\in E_R^\times$ and, for every compact subset $C$ of that set, $$\int_{\{X:\ G(X)\in C\}}\Phi\,d\mu=\int_C g\,d\nu .$$

**Hypothesis (Siegel-Weil formula, convergent range).** For every $F$, $E$, $\sigma$, $M$, $J$ as in the setting, the following two statements hold.

(a) *Finite volume.* $H(\mathbb A)$ has a Haar measure, and for every Haar measure $\mu$ on $H(\mathbb A)$ there is a fundamental domain for the left action of $H(F)$ on $H(\mathbb A)$, and every such fundamental domain has finite $\mu$-measure.

(b) *Coefficients of the theta integral.* Let $n$ be an integer with $2n<M$, and let $T$ be an $n\times n$ matrix over $E$ with $\sigma(T_{ba})=T_{ab}$ and $\det T\ne 0$. Let $b$ be a basis of $E$ over $F$. Let $\Phi$ be a function on $(E_{\mathbb A}^M)^n$ of the form $\Phi(X)=\Phi_\infty(X_\infty)\prod_v\Phi_v(X_v)$, where

- $\Phi_\infty$ is a compactly supported smooth function on $(E_{F_\infty}^M)^n$ (smooth in any real linear coordinates);
- each $\Phi_v$ is a locally constant compactly supported function on $(E_{F_v}^M)^n$, and for all but finitely many $v$ it is the indicator function of the set of tuples all of whose coordinates in the basis $b$ lie in the ring of integers of $F_v$.

Then Haar measures $\mu$ on $H(\mathbb A)$, fundamental domains $\mathcal F$ for $H(F)$, characters $\psi$ of $\mathbb A$ as above, and the self-dual measures $\mu_\infty,\mu_v$ on tuples and $\nu_\infty,\nu_v$ on Hermitian matrices attached to $\psi$ all exist; and for every choice of them there are functions $g_\infty$ on $\mathrm{Herm}_n(F_\infty)$ and $g_v$ on $\mathrm{Herm}_n(F_v)$, one for each finite place $v$, such that

1. $g_\infty$ is a density of $\Phi_\infty$ along the Gram map for $\mu_\infty,\nu_\infty$, and each $g_v$ is a density of $\Phi_v$ along the Gram map for $\mu_v,\nu_v$;
2. the product $\prod_v g_v(T)$ over the finite places converges unconditionally;
3. $$\frac{1}{\mu(\mathcal F)}\int_{\mathcal F}\ \sum_{\substack{X\in (E^M)^n\\ G(X)=T}}\Phi(h^{-1}X)\ d\mu(h)\;=\;g_\infty(T)\prod_v g_v(T).$$

This is Weil's form of Siegel's formula [\[Wei65\]](https://andrewodesky.com/rh/references.html#ref-Wei65) for the unitary group of $J$ and $n$-tuples of vectors, read off at one nondegenerate Fourier coefficient $T$: the average over $H(F)\backslash H(\mathbb A)$ of the part of the theta series supported on tuples with Gram matrix $T$ equals the product of the local densities of $T$ at all places. The condition $2n<M$ implies Weil's convergence condition for every Witt index of $J$. Compared with Weil's theorem, the hypothesis is restricted to factorizable $\Phi$ with compactly supported smooth archimedean component, to nondegenerate $T$, and to $2n<M$; it includes the finiteness of the volume of $H(F)\backslash H(\mathbb A)$ and the existence of continuous local densities as part of what is assumed.
