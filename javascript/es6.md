**使用export和import实现模块化**

// 导出常量
export const sqrt = Math.sqrt;

// 导出函数
export function square(x) {
    return x * x;
}

// 导出函数
export function diag(x, y) {
    return sqrt(square(x) + square(y));
}

export let foo = () => { console.log('haha'); return 'haha'; };

// 一次导出多个
export{ sqrt as sqrt_s , square, diag}

// 导入
import { sqrt_s as sqrt, square, diag } from './lib';
