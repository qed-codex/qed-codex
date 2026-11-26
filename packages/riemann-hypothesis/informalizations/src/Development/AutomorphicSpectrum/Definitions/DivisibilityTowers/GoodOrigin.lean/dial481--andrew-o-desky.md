---
{
  "module": "src/Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/GoodOrigin.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Top.GoodOrigin",
    "GlobalTheory.CompanionTheory.Ar.Top.IsGlobal"
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

## Global models of unitary moduli schemes and geometric origins of root towers

[Definition / hypothesis ARAK.D265](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.IsGlobal/)

This page fixes the arithmetic setting in which root towers are attached to unitary moduli schemes: a *global model* of a moduli scheme, a *geometric origin* of a root tower over such a model, and the *two extra conditions* on an origin. Root models and root towers are those of ([Root towers, their volumes and their slopes](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.RootModel/)).

**The setting.** Use the CM host and the polarized lattice datum of signature $(p,q)$ from the conventions of ([An indefinite polarized CM lattice splits by signature](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitianLatticeSignatureSplit_of_indefinite/)), and the levels, moduli schemes, coefficient fields and models of ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)). Thus $E$ is a CM field; the host supplies a prime $d_0\equiv7\pmod{16}$, an element $r\in\mathcal O_E$ with $r^2=-d_0$ and a complex number $r_0$ with $r_0^2=-d_0$; and $$\Psi=\{\tau:E\hookrightarrow\mathbb C\ :\ \tau(r)=r_0\},\qquad N=p+q .$$ A level has integers $M$ and $A$ and $M'=\operatorname{lcm}(M,A)$. A *family of moduli schemes* is a choice of a moduli scheme $X_l$ of the datum for every level $l$. For a level $l$ with coefficient field $K$, a model $Y$ of $X_l$ is taken over $\mathcal O_K$.

Two real numbers are attached to the host: $$\operatorname{rd}_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]},\qquad \mathcal L_E=\operatorname{Re}\frac{L'(1,\chi)}{L(1,\chi)},$$ where $\chi$ is the quadratic character modulo the prime $d_0$.

**Global models.** Let $(X_l)_l$ be a family of moduli schemes, $l$ a level, $K$ a coefficient field for $l$ and $Y$ a model of $X_l$ over $\mathcal O_K$. The model $Y$ is *global* if the level $l$ is good at every prime number, its integer $A$ equals $1$, and there is, for every prime number $p$ and every valuation subring $W\subset\mathbb C$ in which $p$ is not a unit, a system of local models of the whole family $(X_l)_l$ over $W$, such that the following hold.

- (G1) Every such system carries the level structures, the transition morphisms between its members and the comparison with a Siegel family that the construction of local models requires, and every member of it has split fibres and satisfies the uniformization and specialization conditions of that construction.
- (G2) The model $Y$ descends.
- (G3) For every $p$ and $W$ as above and every ring homomorphism $b$ from $\mathcal O_K$ to the subring of $K$ attached to $W$ that sends each element to itself, the model $Y$ dominates, through $b$, the member of the system at $(p,W)$ that belongs to $(l,K)$.

**Geometric origins.** Let $Y$ be a model as above and let $T$ be a root tower for $(\Psi,N)$, with integer $j$, component set $\mathcal C$, set $S_0$, weight $\nu$ and root models $M_{B,c}$. A *geometric origin* of $T$ over $Y$ consists of data with the following properties.

- (O1) $j=p$.
- (O2) $S_0$ is the set of prime numbers dividing $2\operatorname{disc}(E)\,M'$. For every natural number $B$, put $S_B=\{r\ \text{prime}: r\le B\ \text{or}\ r\in S_0\}$.
- (O3) For every $c\in\mathcal C$ there are a field $\Omega_c$ and a morphism $\xi_c:\operatorname{Spec}\Omega_c\to Y$, the image points of the $\xi_c$ are pairwise distinct, and every generic point of an irreducible component of $Y$ is the image point of some $\xi_c$. There are an integer $m_c\ge0$ and elements $y_{c,0},\dots,y_{c,m_c}\in\Omega_c$ whose ratios generate the field $\Omega_c$; integers $k_{A,c}\ge0$ and $q'_c\ge1$; and integers $n_{c,\tau,i}$ with $$n_{c,\tau,i}=k_{A,c}\,q'_c\,\nu_{\tau,i}\qquad(\tau\in\Psi,\ 0\le i<N).$$
- (O4) For every $c$ there is a complex analytic space $\mathcal X_c$ with a holomorphic atlas, carrying potentials indexed by the variables $X_{\tau,i}$ and $X_0$ of ([Root towers, their volumes and their slopes](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.RootModel/)), and a map $\pi_c:\mathcal X_c\to\mathbb C^{m_c+1}$ with nowhere zero values that is injective up to scalars: $\pi_c(x)=a\,\pi_c(x')$ with $a\in\mathbb C$ implies $x=x'$. The potential indexed by $X_0$ is positive, and its singular and regularized parts vanish. Over $\xi_c$ there are a Lie realization of the semiabelian family of $Y$ and bases of its labelled parts.
- (O5) For every natural number $B$ and every $c$, the root model $M_{B,c}$ is tied to these data: its field contains $\Omega_c$ with finite degree; one of its coordinate blocks consists of the images of $y_{c,0},\dots,y_{c,m_c}$, and its line datum $A$ has degree $1$ on that block and $0$ on the others; its integer $k_A$ is $k_{A,c}$, and its integer $\delta$ is $[K:\mathbb Q]$ times the degree of its flag; its coordinates present a Hodge compactification over $Y$ relative to the set $S_B$, with a complete flag whose graded pieces are presented by the multidegrees of the lines $L_{\tau,i}$ and whose singular metrics are the Hodge norms; and it has an analytic realization over $\mathcal X_c$ in which the lines $L_{\tau,i}(t)$, for small $t>0$, are the successive quotients of the regularized fundamental lines.
- (O6) The origin is *good*: the Hodge compactifications in (O5) satisfy the vector-bundle condition on their differentials; the analytic realizations are smooth and flat; and for every $c$ there is a reference root model with an origin of the kind in (O5) relative to the empty set of primes, of flag degree $1$, with unrestricted coordinate ideal and with an ample rational auxiliary line.

**The two extra conditions.** A geometric origin satisfies the *extra conditions* if both of the following hold.

- (E1) *Local projective immersion.* For every $c$ and every $x\in\mathcal X_c$ there are an open neighbourhood $U$ of $x$ and functions $\lambda_0,\dots,\lambda_{m_c}$ on $\mathcal X_c$, holomorphic on $U$, such that for every $x'\in U$ the vector $(\lambda_i(x'))_i$ is a nonzero scalar multiple of $\pi_c(x')$, and such that, for every index $a$ with $\lambda_a(x)\ne0$ and every chart of the atlas whose domain contains $x$, the derivative at $x$ of $(\lambda_i/\lambda_a)_{0\le i\le m_c}$, computed in that chart, is injective.
- (E2) For every $B$, every $c$ and every $r\in S_B$, the exponent at $r$ of the Hodge compactification of $M_{B,c}$ in (O5) equals $4$.
