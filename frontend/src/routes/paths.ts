import { lazy } from "react";

export const Example = lazy(() => delayForDemo(import("../pages/Example/Example")));
export const NotFound = lazy(() => import('../pages/NotFound/NotFound'))

async function delayForDemo(promise: Promise<any>) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  }).then(() => promise);
}
