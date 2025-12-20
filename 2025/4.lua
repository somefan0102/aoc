local B = arg[1] == "b"
local grid = {}
local total = 0

io.read("a"):gsub("[.@]+", function(r)
    local new = {}
    grid[#grid+1] = new
    r:gsub(".", function(c)
        new[#new+1] = c
    end)
end)

repeat
    local t = {}
    for i=1, #grid do
        for j=1, #grid[i] do
            local count = 0
            if grid[i][j] == "@" then
                for _,nei in ipairs({{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}) do
                    local x, y = i + nei[1], j + nei[2]
                    if x >= 1 and x <= #grid and y >= 1 and y <= #grid[i] then
                        count = count + (grid[x][y] == "@" and 1 or 0)
                    end
                end
                if count < 4 then
                    t[#t+1] = {i, j}
                end
            end
        end
    end
    for i=1, #t do
        grid[t[i][1]][t[i][2]] = "."
    end
    total = total + #t
until #t < 1 or not B

print(total)