function solution(n)
{
    const str=String(n)
    let value=0;
    for(let i=0; i<str.length; i++){
        value+=parseInt(str[i]);
    }
    console.log(value)
    return value
}