// Generated by ScalaTS 0.6.1-SNAPSHOT: https://scala-ts.github.io/scala-ts/

declare var exports: any;

export const nsTransport = exports;

export interface Transport {
  name: string;
}

export function isTransport(v: any): v is Transport {
  return (
    ((typeof v['name']) === 'string')
  );
}
