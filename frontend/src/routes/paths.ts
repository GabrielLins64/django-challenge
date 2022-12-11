import { lazy } from "react";

export const Example = lazy(() => delayForDemo(import("../pages/Example/Example")));

async function delayForDemo(promise: Promise<any>) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  }).then(() => promise);
}
