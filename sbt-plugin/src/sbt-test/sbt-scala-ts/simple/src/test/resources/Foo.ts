// Generated by ScalaTS 0.5.6-SNAPSHOT: https://scala-ts.github.io/scala-ts/

import type { Feature } from './Feature';

export class Foo implements Feature {
  private static instance: Foo;

  private constructor() {}

  public static getInstance() {
    if (!Foo.instance) {
      Foo.instance = new Foo();
    }

    return Foo.instance;
  }
}
