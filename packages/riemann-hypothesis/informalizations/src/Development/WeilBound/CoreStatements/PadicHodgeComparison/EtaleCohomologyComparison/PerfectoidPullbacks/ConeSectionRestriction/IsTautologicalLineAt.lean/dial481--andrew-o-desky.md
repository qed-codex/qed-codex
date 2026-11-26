---
{
  "module": "src/Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/IsTautologicalLineAt.lean",
  "declarations": [
    "CrystallineSemistableComparison.E.LineData.pb",
    "CrystallineSemistableComparison.Pb.CLiftK",
    "CrystallineSemistableComparison.Pb.CLiftK.r"
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

## Logarithmic first Chern class of a line bundle presented by a cocycle of units

[Definition / hypothesis AG.D056](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.IsDlogFirstChernClass/)

**Presentations of a line bundle.** Let $X$ be a scheme. A *presentation of a line bundle* on $X$ is a pair $(f,u)$ in which $f:Y\to X$ is a smooth surjective morphism of schemes and $u$ assigns to every scheme $S$ and every pair of morphisms $s,t:S\to Y$ with $f\circ s=f\circ t$ a unit $u(s,t)\in\mathcal O_S(S)^\times$, subject to two conditions:

1. $u(s\circ g,t\circ g)=g^*u(s,t)$ for every morphism of schemes $g:S'\to S$;
2. $u(s,t)\,u(t,t')=u(s,t')$ whenever $f\circ s=f\circ t=f\circ t'$.

Thus $u$ is a cocycle with values in $\mathbb G_m$ on the Čech nerve of $f$; it is the gluing datum of a line bundle on $X$ that is trivialized over $Y$. For a morphism of schemes $g:X'\to X$, the *pullback* of $(f,u)$ to $X'$ is the presentation $(f',u')$ on $X'$ in which $f':Y\times_XX'\to X'$ is the second projection and $u'(s,t)=u(\mathrm{pr}_1\circ s,\mathrm{pr}_1\circ t)$, where $\mathrm{pr}_1:Y\times_XX'\to Y$ is the first projection.

Now let $K$ be a commutative ring, let $X$ be a scheme over $K$, and let $(f:Y\to X,u)$ be a presentation of a line bundle on $X$. In outline, a logarithmic first Chern class of $(f,u)$ is a class in the group $H^2_1(X/K)$ of ([Graded infinitesimal cohomology](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.Hdg/)) with the following property: on every diagram of divided-power thickenings of $X$ on which the units given by $u$ have been lifted to units $w$ of the thickenings, the class is represented by the cocycle $\sigma\mapsto r(\sigma)-1$, where the unit $r(\sigma)$ measures by how much the lifts $w$ fail the cocycle condition 2. The next three paragraphs define the lifts, the restriction of a class to a diagram, and the class.

**Lifts along a diagram of thickenings.** Use the category $\operatorname{Thick}(X/K)$, the ideals $J^{[r]}$, the modules $\operatorname{gr}^a$, the groups $H^n_a(X/K)$ and the universes $\mathcal U\in\mathcal U'$ of ([Graded infinitesimal cohomology](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.Hdg/)). Let $\mathcal D$ be a category with sets of morphisms in $\mathcal U$ and a set of objects in $\mathcal U'$, and let $G:\mathcal D\to\operatorname{Thick}(X/K)$ be a functor. Write $G(D)=(B_D,J_D,\delta_D,y_D)$ for an object $D$ of $\mathcal D$, and for a morphism $\varphi:D\to D'$ of $\mathcal D$ write $\varphi_*:B_D\to B_{D'}$ for the homomorphism $G(\varphi)$ and $\bar\varphi:B_D/J_D\to B_{D'}/J_{D'}$ for the homomorphism that it induces. A *lift of $(f,u)$ along $G$* is a pair $(p,w)$ consisting of

- for every object $D$, a morphism $p_D:\operatorname{Spec}(B_D/J_D)\to Y$ with $f\circ p_D=y_D$;
- for every morphism $\varphi:D\to D'$, a unit $w(\varphi)\in B_{D'}^\times$ whose image in $B_{D'}/J_{D'}$ is $u\bigl(p_D\circ\operatorname{Spec}(\bar\varphi),\,p_{D'}\bigr)$, a unit of the ring of global functions $B_{D'}/J_{D'}$ of $\operatorname{Spec}(B_{D'}/J_{D'})$.

For a pair of composable morphisms $\sigma=(D_0\xrightarrow{\varphi}D_1\xrightarrow{\psi}D_2)$ of $\mathcal D$ put $$r(\sigma)=\psi_*\bigl(w(\varphi)\bigr)\,w(\psi)\,w(\psi\circ\varphi)^{-1}\in B_{D_2}^\times.$$ By conditions 1 and 2 on $u$ and the condition on the images of the units $w(\varphi)$, the image of $r(\sigma)$ in $B_{D_2}/J_{D_2}$ is $1$, so that $r(\sigma)-1\in J_{D_2}$.

**Restriction to a diagram.** For $G$ as above and $a\ge0$, the cochains, differential and cohomology of ([Graded infinitesimal cohomology](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.Hdg/)) are defined in the same way for chains of composable morphisms of $\mathcal D$ and the modules $\operatorname{gr}^a(G(D))$; write $H^n_a(G)$ for the resulting cohomology groups. Sending a cochain $\alpha$ on $\operatorname{Thick}(X/K)$ to the cochain $\sigma\mapsto\alpha(G(\sigma))$ on $\mathcal D$ commutes with the differentials and defines a $K$-linear map $G^*:H^n_a(X/K)\to H^n_a(G)$.

**The logarithmic first Chern class.** A class $c\in H^2_1(X/K)$ is a *logarithmic first Chern class* of $(f,u)$ if the following holds for every category $\mathcal D$ as above, every functor $G:\mathcal D\to\operatorname{Thick}(X/K)$ such that for each object $D$ of $\mathcal D$ the morphism $y_D$ factors through an open subscheme of $X$ over which $f$ has a section, and every lift $(p,w)$ of $(f,u)$ along $G$: there is a $2$-cocycle $z$ on $\mathcal D$ with values in $\operatorname{gr}^1$ whose class is $G^*c$ and such that, for every pair of composable morphisms $\sigma=(D_0\to D_1\to D_2)$ of $\mathcal D$, $$z(\sigma)=r(\sigma)-1\quad\text{in }B_{D_2}/J_{D_2}^{[2]},$$ where $z(\sigma)\in\operatorname{gr}^1(G(D_2))=J_{D_2}/J_{D_2}^{[2]}$ is regarded as an element of $B_{D_2}/J_{D_2}^{[2]}$. The name refers to the map $1+x\mapsto x$ from the group $1+J_{D_2}$ under multiplication to $J_{D_2}/J_{D_2}^{[2]}$: it is a homomorphism, because the product of two elements of $J_{D_2}$ lies in $J_{D_2}^{[2]}$, and it takes the place of the logarithm.
