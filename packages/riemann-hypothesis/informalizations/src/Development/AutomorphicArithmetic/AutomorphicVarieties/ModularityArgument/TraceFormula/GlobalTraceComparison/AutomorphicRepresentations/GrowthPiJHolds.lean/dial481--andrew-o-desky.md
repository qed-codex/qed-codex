---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/AutomorphicRepresentations/GrowthPiJHolds.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.growthPiJ_holds"
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

## A quantitative twisted trace comparison

[Theorem REP.0073](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.growthPiJ_holds/)

Let $E$ be a CM number field with at least two infinite places, and let $n\ge1$. Give $G_n=\mathrm{GL}_n(\mathbb A_E)$ and $G_0=\mathrm{GL}_0(\mathbb A_E)$ their Borel measurable structures and arbitrary Haar measures $\mu_1,\mu_2$. There is a Haar and arithmetic-quotient datum $D$ on $G_n\times G_0$ whose group measure integrates every continuous compactly supported function as the iterated integral against $\mu_1,\mu_2$.

Let $\pi$ be a cuspidal representation whose functions are invariant under the real split center and whose space is preserved by the specified conjugate-inverse-transpose involution $\theta$. For a finite index set $I$, let $\mathcal H=L^2(D)^I$ and let $P\subset\mathcal H$ be the closed span of vectors with components $\psi(g)u(\log|\det g|)$, where $\psi\in\pi$ and $u$ is continuous and compactly supported. Fix matrices of continuous compactly supported test functions $\Phi_1,\Phi_2$, their quotient-kernel operators $T_1,T_2$, a matrix $M\in\operatorname{Mat}_I(\mathbb C)$, and $r_0,r_1\ge0$, $\varepsilon>0$. For each entry of $\Phi_1$, assume one fixed finite-dimensional subspace of $\pi$ contains its convolution images for every continuous multiplier $u(\log|\det|)$ and every vector of $\pi$.

There are $C\in\mathbb R$ and $N\in\mathbb Z_{\ge0}$ such that for every integer $k\ge0$, bounded complex-linear $U:\mathcal H\to\mathcal H$ preserving $P$ and $P^\perp$, and test matrix $\Phi$ with quotient operator $T_1UT_2$, the following holds. Put $\phi(g)=\operatorname{tr}(\Phi(g)M)$. Suppose $\phi$ satisfies all the slice, support and level conditions below with bound $r_0+kr_1$. If its $\theta$-twisted convolution on $\pi$ has finite-dimensional image and trace $t$, then $$\left|\mathcal E(\phi)-\frac t2\right|\le C(1+k)^N\|U|_{P^\perp}\|+C\|U\|\varepsilon^k.$$ Here $\mathcal E(\phi)$ is the sum of twisted orbital integrals over pairs of rational twisted conjugacy classes represented by $d$ such that $d\theta(d)$ has separable characteristic polynomial and all its roots have modulus $1$ at every complex embedding, in each factor; the rational twisted centralizers carry counting measure.
