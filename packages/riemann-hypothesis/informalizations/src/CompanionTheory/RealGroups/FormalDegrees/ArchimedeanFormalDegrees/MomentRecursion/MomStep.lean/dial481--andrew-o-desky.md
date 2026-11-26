---
{
  "module": "src/CompanionTheory/RealGroups/FormalDegrees/ArchimedeanFormalDegrees/MomentRecursion/MomStep.lean",
  "declarations": [
    "CompanionTheory.RgFd.momA"
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

## Positive moments determine the measure of a support

[Theorem ALG.1290](https://andrewodesky.com/rh/lean/CompanionTheory.RgFd.momA/)

Let $(\Omega,\nu)$ and $(\Omega',\nu')$ be measure spaces, with no finiteness assumption on their total measures. Let $U:\Omega\to[0,1]$ and $U':\Omega'\to[0,1]$ be measurable, and let $t_0\ge1$ be an integer. Suppose that for every integer $j\ge1$, $$\int_\Omega U^{jt_0}\,d\nu=\int_{\Omega'}(U')^{jt_0}\,d\nu'<\infty.$$ Then $$\nu\{x:U(x)>0\}=\nu'\{y:U'(y)>0\}.$$ The integrals and the conclusion are understood in the nonnegative extended sense.
