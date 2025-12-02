local B = arg[1] == "b"
local p = 50
local zeroes = 0

for rot, dist in io.read("a"):gmatch("([LR])(%d+)") do
    dist = tonumber(dist)
    for i = 1, dist do
        p = (p + (rot == "L" and -1 or 1)) % 100
        if p == 0 and (((i == dist) and not B) or B) then
            zeroes = zeroes + 1
        end
    end
end

print(zeroes)